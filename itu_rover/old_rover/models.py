from django.db import models
from django.db.models import ObjectDoesNotExist

from core.models import TimeStampedModel
from .utils import validate_one_object, get_upload_path


class AddRover(models.Model):
    rover_name = models.CharField(max_length=25)

    class Meta:
        ordering = ('rover_name',)

    def __str__(self):
        return self.rover_name

class Person(models.Model):
    """ Abstract base class representing a person """
    first_name = models.CharField(
        max_length=25,
        db_index=True,
        verbose_name='first name',
    )
    last_name = models.CharField(
        max_length=25,
        verbose_name='last name',
    )
    email = models.EmailField(
        blank=True,
        verbose_name='email address'
    )
    photo = models.ImageField(
        upload_to=get_upload_path,
        verbose_name='photo'
    )
    phone = models.CharField(
        max_length=13,
        blank=True,
        verbose_name='phone number',
    )
    is_retired = models.BooleanField(
        default=False,
        verbose_name='is member retired?',
    )
    class Meta:
        abstract = True
        ordering = ('first_name', 'last_name')

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_photo_url(self):
        if not self.photo:
            return "default/photo.url"
        return self.photo.url

    def __str__(self):
        return self.get_full_name()


class Member(Person, TimeStampedModel):
    """ Team member model, a member is a person. """
    subteam = models.ForeignKey(
        "SubTeam",
        on_delete=models.SET_NULL,  #when you delete a User, you might want to keep the comments he posted on blog posts,
        related_name='members',
        blank=True,
        null=True,
        verbose_name='subteam of member',
    )
    rover_years = models.ForeignKey(
        'AddRover',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='member_of',
        verbose_name='member name',
    )
    description = models.CharField(
        max_length=75,
        blank=True,
        verbose_name='description (e.g. department)',
    )
    def role(self):
        subteam_str = str(self.subteam)
        is_old = " Eski" if self.is_retired else ""

        try:
            is_team_leader = bool(self.leader)
        except ObjectDoesNotExist:
            is_team_leader = False

        if self.subteam and self.subteam.leader == self:
            return subteam_str + " Lideri"
        elif is_team_leader:
            return "Takım Lideri"
        elif not self.subteam:
            return "Ekip Üyesi"
        return subteam_str + is_old + " Üyesi"


class SubTeam(models.Model):
    """
    A subteam represents a group of people who work for the same
    specific domain of the project. For instance; mechanical subteam.
    """
    name = models.CharField(
        max_length=50,
        db_index=True,
        verbose_name='subteam name',
    )
    leader = models.OneToOneField(
        'Member',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='leader_of',
        verbose_name='subteam leader',
    )

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class TeamLeader(models.Model):
    """ Leader of the whole team """
    member = models.OneToOneField(
        'Member',
        on_delete=models.SET_NULL,
        null=True,
        related_name='leader',
        verbose_name='team leader',
    )

    class Meta:
        verbose_name = "team leader"
        verbose_name_plural = verbose_name

    def clean(self):
        validate_one_object(self)

    def __str__(self):
        return str(self.member)


class TeamAdvisor(Person, TimeStampedModel):
    description = models.CharField(
        max_length=75,
        verbose_name='description (e.g. department)',
    )

    def role(self):
        return "Takım Danışmanı"


class MembersPage(models.Model):
    proposal = models.FileField(
        upload_to='documents/team',
        blank=True,
    )
    team_photo = models.ImageField(
        upload_to='images/members',
        blank=True,
    )

    def clean(self):
        validate_one_object(self)

    def __str__(self):
        return "Members Page"

    class Meta:
        verbose_name = "Members Page"
        verbose_name_plural = verbose_name
