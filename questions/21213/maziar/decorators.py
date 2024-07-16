from functools import wraps
from django.http import HttpResponse,HttpResponseForbidden
from .models import ProjectMembership


# noinspection PyPep8Naming
class projects_panel(object):
    def __init__(self, permissions=None):
        self.permissions = permissions

    def __call__(self, view_func):

        @wraps(view_func)
        def _wrapper_view(request, *args, **kwargs):
            # Step 1: Check if the user has any projects
            if not request.user.projects.exists():
                return HttpResponse("No projects found", status=404)
            request.memberships=request.user.projects.filter(user=request.user.id)
            # Step 2: Get the user's current membership and project
            try:
                request.current_membership = request.user.projects.get(is_current=True)
            except ProjectMembership.DoesNotExist:
                request.current_membership = request.user.projects.order_by('id').first()

            request.project = request.current_membership.project

            # Step 3: Check permissions if provided
            if self.permissions:
                if not all(request.current_membership.has_permission(permission) for permission in self.permissions):
                    return HttpResponseForbidden("Forbidden", status=403)

            # Call the original view function with the modified request object
            return view_func(request, *args, **kwargs)

        return _wrapper_view