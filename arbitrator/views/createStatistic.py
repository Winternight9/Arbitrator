import sys

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from arbitrator.models import Statistic
from django.shortcuts import redirect


@login_required
def createStat(request):
    id = request.user.id
    create = True
    check_id = Statistic.objects.filter(user_id=id)
    for check in check_id:
        if check.user_id == id:
            create = False
    if create == True:
        user = User.objects.get(pk=id)
        stat = Statistic(user=user)
        stat.save()
    return redirect('arbitrator:home')   

sys.modules[__name__] = createStat

        

