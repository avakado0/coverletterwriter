work_interval = 25 * 60  # 25 minutes in seconds
break_interval = 5 * 60  # 5 minutes in seconds


# Loop through each task in the cover letter generation process
for task in cover_letter_tasks:
    print(f"Working on: {task}")

    # Work for the specified interval
    time.sleep(work_interval)

    # Take a break for the specified interval
    time.sleep(break_interval)

# Inside your code loop
for task in cover_letter_tasks:
    # Display a notification to take a break
    notification.notify(
        title="Take a Break",
        message="It's time for a short break!",
        timeout=10  # Display for 10 seconds
    )

    # Work for the specified interval
    time.sleep(work_interval)
