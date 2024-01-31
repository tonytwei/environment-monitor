from datetime import datetime, timedelta


start_time = datetime.now() - timedelta(days=20)
end_time = datetime.now() - timedelta(hours=1)
iso_start_time = start_time.isoformat() + "Z"
iso_end_time = end_time.isoformat() + "Z"

print(iso_start_time)
print(iso_end_time)