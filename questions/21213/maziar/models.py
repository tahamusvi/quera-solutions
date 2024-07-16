from django.contrib.auth.models import User
from django.db import models, transaction


class Project(models.Model):
    name = models.CharField(max_length=100)


class ProjectMembership(models.Model):
    ROLE_GUEST = 'RG'
    ROLE_REPORTER = 'RR'
    ROLE_DEVELOPER = 'RD'
    ROLE_MASTER = 'RM'
    ROLE_OWNER = 'RO'

    ROLE_CHOICES = (
        (ROLE_GUEST, 'Guest'),
        (ROLE_REPORTER, 'Reporter'),
        (ROLE_DEVELOPER, 'Developer'),
        (ROLE_MASTER, 'Master'),
        (ROLE_OWNER, 'Owner'),

    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    role = models.CharField(max_length=4, choices=ROLE_CHOICES, default=ROLE_GUEST, verbose_name='Role')
    is_current = models.BooleanField(default=False)



    def has_permission(self, action):
        # Convert snake_case action to title case for comparison
        action = action.replace('_', ' ').title()
        # Check the user's role and return True or False based on the permission table
        if self.role == 'RG':
            return action in ['Create New Issue', 'Leave Comments']
        elif self.role == 'RR':
            return action in ['Create New Issue', 'Leave Comments', 'Pull Project Code']
        elif self.role == 'RD':
            return action in [
                'Create New Issue',
                'Leave Comments',
                'Pull Project Code',
                'Assign Issues And Merge Requests',
                'See A List Of Merge Requests',
                'Create New Branches',
            ]
        elif self.role == 'RM':
            return action in [
                'Create New Issue',
                'Leave Comments',
                'Pull Project Code',
                'Assign Issues And Merge Requests',
                'See A List Of Merge Requests',
                'Manage Merge Requests',
                'Create New Branches',
                'Add New Team Members',
                'Push To Protected Branches',
            ]
        elif self.role == 'RO':
            return action in [
                'Create New Issue',
                'Leave Comments',
                'Pull Project Code',
                'Assign Issues And Merge Requests',
                'See A List Of Merge Requests',
                'Manage Merge Requests',
                'Create New Branches',
                'Add New Team Members',
                'Push To Protected Branches',
                'Switch Visibility Level',
                'Remove Project',
            ]

    class Meta:
        unique_together = ('user', 'project')


