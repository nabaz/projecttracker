from api.views.customer_viewset import CustomerViewSet
from api.views.project_viewset import ProjectViewSet
from api.views.task_viewset import TaskViewSet
from api.views.time_entry_viewset import TimeEntryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/customers', CustomerViewSet, base_name='customer')
router.register(r'api/projects', ProjectViewSet, base_name='project')
router.register(r'api/tasks', TaskViewSet, base_name='task')
router.register(r'api/time-entries', TimeEntryViewSet, base_name='time-entry')

urlpatterns = router.urls
