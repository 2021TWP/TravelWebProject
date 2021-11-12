from django.db import models

class Schedule(models.Model):
    objects = models.Manager()
    # group_id = models.ForeignKey(Group, on_delete=models.CASCADE())
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=300)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=400)
    # img = models.TextField(max_length=500,null=True,blank=True )
    lat = models.CharField(max_length=300)
    lng = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id)

class Schedule_content(models.Model):
    # 일반적으론 Schedule 번호(id)를 갖고 있음.
    # 동일하게 유저에서 그룹의 id를 갖고 있어서 정보를 참조할 수 있겠끔

    #원본 데이터를 넣어두고 레퍼랜스 하게
    objects = models.Manager()
    content = models.TextField()
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    # travel_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.id)
