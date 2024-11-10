def main():
    n = int(input("Enter the number of processes: "))
    
    # Initialize lists for process IDs, burst times, priorities, waiting times, and turnaround times
    p = [0] * 10
    pp = [0] * 10
    bt = [0] * 10
    w = [0] * 10
    t = [0] * 10

    print("Enter the burst time and priority for each process:")

    # Input burst times and priorities for each process
    for i in range(n):
        print(f"Process[{i + 1}]")
        bt[i] = int(input("Burst Time: "))
        pp[i] = int(input("Priority: "))
        p[i] = i + 1  # Process ID is simply i+1 (1-based index)

    # Sort the processes by priority (higher priority comes first)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if pp[i] < pp[j]:
                # Swap priorities
                pp[i], pp[j] = pp[j], pp[i]
                # Swap burst times
                bt[i], bt[j] = bt[j], bt[i]
                # Swap process IDs
                p[i], p[j] = p[j], p[i]

    # Initialize waiting time and turnaround time
    w[0] = 0  # Waiting time for the first process is always 0
    awt = 0  # Average waiting time
    t[0] = bt[0]  # Turnaround time for the first process is its burst time
    atat = t[0]  # Average turnaround time starts with the first process turnaround time

    # Calculate waiting time and turnaround time for each process
    for i in range(1, n):
        w[i] = t[i - 1]  # Waiting time of process i is the turnaround time of the previous process
        awt += w[i]  # Accumulate total waiting time
        t[i] = w[i] + bt[i]  # Turnaround time is waiting time + burst time
        atat += t[i]  # Accumulate total turnaround time

    # Print process details
    print("Process \t Burst time \t Wait time \t TAT \t Priority")
    for i in range(n):
        print(f"{p[i]}\t\t{bt[i]}\t\t{w[i]}\t\t{t[i]}\t\t{pp[i]}")

    # Calculate average waiting time and average turnaround time
    awt /= n
    atat /= n

    # Print average waiting time and turnaround time
    print(f"Average Wait time: {awt:.5f}")
    print(f"Average TAT: {atat:.5f}")

if __name__ == "__main__":
    main()
