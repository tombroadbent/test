from datetime import datetime, timedelta

gender = str(input('What is your gender? (M/F) ')).lower()
if gender != 'm' and gender != 'f':
    print("error message")

if gender == 'm':
    duration = 104 #weeks
elif gender == 'f':
    duration = 72 #weeks

start_dateStr = str(input('What is your start date? (YYYY-MM-DD) '))
start_date = datetime.strptime(start_dateStr, '%Y-%m-%d')
completion_date = start_date + timedelta(weeks=duration)
print(completion_date.strftime('%Y-%m-%d'))
print()

transfer_dateStr = str(input('What is the next transfer date? (YYYY-MM-DD) '))
transfer_date = datetime.strptime(transfer_dateStr, '%Y-%m-%d')
if transfer_date >= completion_date:
    print("Must be less than completion date")

transferBeforeCompletion = transfer_date
transferAfterCompletion = transfer_date + timedelta(weeks=6)

while transferAfterCompletion < completion_date:
    transferBeforeCompletion = transferAfterCompletion
    transferAfterCompletion = transferBeforeCompletion + timedelta(weeks=6)

print("Closest transfer date before completion:", transferBeforeCompletion.strftime('%Y-%m-%d'))
print("Closest transfer date after completion:", transferAfterCompletion.strftime('%Y-%m-%d'))


