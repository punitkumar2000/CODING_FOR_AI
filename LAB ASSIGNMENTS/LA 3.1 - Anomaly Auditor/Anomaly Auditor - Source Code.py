telemetry_stream = [
    [22.5, 23.0, 22.8],
    [25.1, "ERR", 24.9],
    [30.2, 35.5, 40.1],  # Threshold breach
    [22.0, 22.1, "STOP"],  # Termination signal
]

shutdown_triggered = False

for batch_id in range(len(telemetry_stream)):
    previous_value = None
    print(f"--- Auditing Batch {batch_id}: {telemetry_stream[batch_id]} ---")
    batches = telemetry_stream[batch_id]

    for reading in batches:
        if reading == "STOP":
            print(f"Emergency Shutdown at Batch {batch_id}.")
            shutdown_triggered = True
            break

        if reading == "ERR":
            print(f"Noise ignored at Batch {batch_id} (ERR).")
            continue

        if isinstance(reading, (int, float)):
            if reading > 35.0:
                print("Anomaly Detected at Batch", batch_id, ":", reading)

            if previous_value is not None:
                delta = abs(reading - previous_value)

                if delta > 5.0:
                    print(
                        f"Spike detected at {batch_id}: "
                        f"{previous_value} -> {reading} "
                        f"Delta {delta:.1f}"
                    )

            previous_value = reading

    if shutdown_triggered:
        break

else:
    print("Audit Complete : No system-wide failures")