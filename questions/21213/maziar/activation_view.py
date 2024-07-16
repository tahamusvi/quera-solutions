from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from projects.models import Project, ProjectMembership


@login_required
def active_project(request, project_id):

    project = get_object_or_404(Project, id=project_id)
    membership = ProjectMembership.objects.get(project=project, user=request.user)

    ProjectMembership.objects.filter(user=request.user).exclude(id=membership.id).update(is_current=False)
    membership.is_current = True
    membership.save()

    if not project or not membership:
        return redirect('index', status=404)

    return redirect('index',statis=200)

