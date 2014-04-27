from mezzanine.pages.page_processors import processor_for
from .models import UserProfile


@processor_for("members")
def members_list(request, page):
	members = UserProfile.objects.all()
	return {"members": members}