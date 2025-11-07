from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import RequestLog, SuspiciousIP

SENSITIVE_PATHS = ['/admin', '/login']

@shared_task
def detect_anomalies():
    one_hour_ago = timezone.now() - timedelta(hours=1)

    # count of requests per IP in last hour
    logs = (RequestLog.objects
            .filter(timestamp__gte=one_hour_ago)
            .values('ip_address')
            .annotate(count=models.Count('id')))

    for record in logs:
        if record['count'] > 100:
            SuspiciousIP.objects.get_or_create(
                ip_address=record['ip_address'],
                reason="More than 100 requests in one hour"
            )

    # detect access to sensitive paths
    sensitive_logs = RequestLog.objects.filter(
        timestamp__gte=one_hour_ago,
        path__in=SENSITIVE_PATHS
    ).values_list('ip_address', 'path')

    for ip, path in sensitive_logs:
        SuspiciousIP.objects.get_or_create(
            ip_address=ip,
            reason=f"Accessed sensitive path: {path}"
        )
