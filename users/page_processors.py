from mezzanine.pages.page_processors import processor_for
from .models import UserProfile


@processor_for("members")
def members_list(request, page):
	members = UserProfile.objects.all()
	voting_members = members.filter(type="Voting")
	caucus_members = members.filter(type="Caucus")
	association_members = members.filter(type="Association")
	return {
	"members": members, 
	"voting_members": voting_members, 
	"caucus_members": caucus_members, 
	"association_members": association_members
	}