from api.views.customer_viewset import CustomerViewSet
from api.views.project_viewset import ProjectViewSet
from api.views.task_viewset import TaskViewSet
from api.views.time_entry_viewset import TimeEntryViewSet
from rest_framework.routers import DefaultRouter

from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'api/customers', CustomerViewSet, base_name='customer')
# router.register(r'^api/customer/(?P<pk>[0-9]+)$', CustomerViewSet, base_name='customer')
router.register(r'api/projects', ProjectViewSet, base_name='project')
router.register(r'api/tasks', TaskViewSet, base_name='task')
router.register(r'api/time-entries', TimeEntryViewSet, base_name='time-entry')

# urlpatterns = [
#     url(r'^api/customers$', viewsets.CustomerViewSet),
#     url(r'^api/projects$', views.ProjectView.as_view()),
#     url(r'^api/tasks$', views.TaskView.as_view()),
#     url(r'^api/time-entries$', views.TimeEntryView.as_view()),
#     url(r'^api/customer/(?P<pk>[0-9]+)$', views.CustomerDetailView.as_view()),
#     url(r'^api/', obtain_jwt_token),
#
# ]
urlpatterns = router.urls
