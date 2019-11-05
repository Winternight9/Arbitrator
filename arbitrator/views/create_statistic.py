
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from arbitrator.models import Statistic



@login_required
def create_stat(request):
    id = request.user.id
    create = True
    check_id = Statistic.objects.filter(user_id=id)
    for check in check_id:
        if check.user_id == id:
            check_id = False
    if create == True:
        user = User.objects.get(pk=id)
        stat = Statistic(user=user)
        stat.save()

        

