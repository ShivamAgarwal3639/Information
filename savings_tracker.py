import datetime
from dateutil.relativedelta import relativedelta
from icalendar import Calendar, Event, Alarm
import os

# =============================================================================
# CONFIGURATION
# =============================================================================
INTEREST_RATE = 0.025  # 2.5% monthly interest
INITIAL_MONTHLY_SAVING = 5800  # Starting savings (April 2025)
START_DATE = datetime.date(2025, 4, 1)
END_DATE = datetime.date(2035, 10, 1)
OUTPUT_DIR = "retirement_plan"
RUPEES_SYMBOL = "₹"

# =============================================================================
# GENERATE MONTHLY SAVINGS SCHEDULE
# =============================================================================
def generate_savings_schedule():
    current_date = START_DATE
    current_rate = INITIAL_MONTHLY_SAVING
    schedule = []
    
    while current_date <= END_DATE:
        if current_date.month == 11 and current_date.year >= 2025:
            current_rate = int(round(current_rate * 1.2))
        
        schedule.append({
            "year": current_date.year,
            "month": current_date.strftime("%B"),
            "rate": current_rate,
            "date_obj": current_date
        })
        
        current_date += relativedelta(months=1)
    
    return schedule

# =============================================================================
# CALCULATE ACCUMULATED SAVINGS
# =============================================================================
def calculate_accumulations(schedule):
    accumulated = 0
    detailed_schedule = []
    
    for month in schedule:
        detailed_schedule.append({
            "year": month["year"],
            "month": month["month"],
            "pre_accumulated": round(accumulated, 2),
            "rate": month["rate"]
        })
        
        accumulated = (accumulated + month["rate"]) * (1 + INTEREST_RATE)
    
    return detailed_schedule

# =============================================================================
# GENERATE MARKDOWN FILE
# =============================================================================
def generate_markdown(schedule):
    md = f"""# Retirement Savings Tracker (2.5% Monthly Interest)

**Start**: April 2025  
**Target**: October 2035  
**Monthly Interest**: 2.5%  
**Savings Policy**: 20% annual increment every November

| Status | Year | Month | Pre-Accumulated ({RUPEES_SYMBOL}) | Monthly Saving ({RUPEES_SYMBOL}) |
|--------|------|-------|----------------------|--------------------|
"""
    
    for entry in schedule:
        md += f"| [ ] | {entry['year']} | {entry['month']} | {int(entry['pre_accumulated']):,} | {entry['rate']:,} |\n"
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "savings_tracker.md"), "w", encoding="utf-8") as f:
        f.write(md)

# =============================================================================
# GENERATE CALENDAR REMINDERS (FIXED ALARM TRIGGER)
# =============================================================================
def generate_calendar(schedule):
    cal = Calendar()
    cal.add('prodid', '-//Retirement Savings Reminder//mxm.dk//')
    cal.add('version', '2.0')

    for entry in schedule:
        event = Event()
        event.add('summary', '💰 Retirement Savings Deposit')
        event.add('description', 
                 f"Month: {entry['month']} {entry['year']}\n"
                 f"Amount: {RUPEES_SYMBOL}{entry['rate']:,}\n"
                 "Status: Pending [ ] / Completed [X]")
        
        event_date = datetime.date(entry['date_obj'].year, entry['date_obj'].month, 5)
        event.add('dtstart', event_date)
        event.add('dtend', event_date)
        event.add('dtstamp', datetime.datetime.now())
        
        # Add alarm with proper trigger type
        alarm = Alarm()
        alarm.add('action', 'DISPLAY')
        alarm.add('description', 'Reminder: Savings deposit due tomorrow!')
        alarm.add('trigger', datetime.timedelta(days=-1))  # Fixed trigger type
        event.add_component(alarm)
        
        cal.add_component(event)

    with open(os.path.join(OUTPUT_DIR, "savings_reminder.ics"), "wb") as f:
        f.write(cal.to_ical())

# =============================================================================
# MAIN EXECUTION
# =============================================================================
if __name__ == "__main__":
    schedule = generate_savings_schedule()
    detailed_schedule = calculate_accumulations(schedule)
    generate_markdown(detailed_schedule)
    generate_calendar(schedule)
    print(f"Files generated in '{OUTPUT_DIR}' directory!")
