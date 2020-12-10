from delegates.models import Delegate


all_delegates=Delegate.objects.all()

for delegate in all_delegates:
	