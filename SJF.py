def main():
    # Taking the number of processes
    n = int(input("Enter number of processes: "))
    
    # Matrix for storing Process Id, Burst Time, Waiting Time & Turn Around Time
    A = [[0 for j in range(4)] for i in range(n)]
    total, avg_wt, avg_tat = 0, 0, 0
    
    print("Enter Burst Time:")
    
    # User Input Burst Time and allocating Process Id
    for i in range(n):
        A[i][0] = i + 1  # Process ID (1, 2, 3, ...)
        A[i][1] = int(input(f"P{i+1}: "))  # Burst time for each process
    
    # Sorting processes according to their Burst Time using simple Bubble Sort
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if A[j][1] < A[index][1]:
                index = j
        # Swap burst time
        temp = A[i][1]
        A[i][1] = A[index][1]
        A[index][1] = temp
        
        # Swap process ID
        temp = A[i][0]
        A[i][0] = A[index][0]
        A[index][0] = temp
    
    # Initializing Waiting Time for the first process
    A[0][2] = 0
    
    # Calculate Waiting Time (WT) for each process
    for i in range(1, n):
        A[i][2] = 0
        for j in range(i):
            A[i][2] += A[j][1]
    
    # Calculate Total Waiting Time
    total = sum([A[i][2] for i in range(n)])
    avg_wt = total / n
    
    # Calculation of Turnaround Time (TAT) and printing the data
    # P = Processes, BT = Burst time, WT = Waiting time, TAT = Turnaround time
    print("P\tBT\tWT\tTAT")
    
    total = 0
    for i in range(n):
        A[i][3] = A[i][1] + A[i][2]  # TAT = BT + WT
        total += A[i][3]
        print(f"P{A[i][0]}\t{A[i][1]}\t{A[i][2]}\t{A[i][3]}")
    
    avg_tat = total / n
    
    print(f"Average Waiting Time = {avg_wt}")
    print(f"Average Turnaround Time = {avg_tat}")


if __name__ == "__main__":
    main()
