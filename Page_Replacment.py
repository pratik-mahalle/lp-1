from collections import deque

# FIFO (First In, First Out) page replacement algorithm
def fifo(page_sequence, frame_count):
    frames = []
    page_faults = 0
    
    for page in page_sequence:
        if page not in frames:
            page_faults += 1
            if len(frames) >= frame_count:
                frames.pop(0)  # Remove the oldest page (FIFO)
            frames.append(page)
    
    return page_faults

# Optimal page replacement algorithm
def optimal(page_sequence, frame_count):
    frames = []
    page_faults = 0
    
    for i in range(len(page_sequence)):
        page = page_sequence[i]
        
        if page not in frames:
            page_faults += 1
            if len(frames) >= frame_count:
                # Find the page that will not be used for the longest time
                farthest = -1
                farthest_idx = -1
                for j in range(len(frames)):
                    try:
                        next_use = page_sequence[i+1:].index(frames[j])
                    except ValueError:
                        next_use = float('inf')  # If page is not found in future, it will be replaced
                    if next_use > farthest:
                        farthest = next_use
                        farthest_idx = j
                frames[farthest_idx] = page
            else:
                frames.append(page)
                
    return page_faults

# LRU (Least Recently Used) page replacement algorithm
def lru(page_sequence, frame_count):
    frames = []
    page_faults = 0
    recent_use = {}  # Dictionary to keep track of last use of each page
    
    for i in range(len(page_sequence)):
        page = page_sequence[i]
        
        if page not in frames:
            page_faults += 1
            if len(frames) >= frame_count:
                # Find the least recently used page
                lru_page = min(recent_use, key=recent_use.get)
                frames.remove(lru_page)
            frames.append(page)
        
        recent_use[page] = i  # Update the most recent use time of the page
    
    return page_faults

# Function to input data and simulate page replacement
def simulate_page_replacement():
    # Input the page sequence and the number of frames
    page_sequence = list(map(int, input("Enter the page reference string (space-separated): ").split()))
    frame_count = int(input("Enter the number of frames: "))
    
    # Simulate page replacement for FIFO, Optimal, and LRU
    print("\nSimulating FIFO...")
    fifo_faults = fifo(page_sequence, frame_count)
    print(f"FIFO: Number of page faults: {fifo_faults}")
    
    print("\nSimulating Optimal...")
    optimal_faults = optimal(page_sequence, frame_count)
    print(f"Optimal: Number of page faults: {optimal_faults}")
    
    print("\nSimulating LRU...")
    lru_faults = lru(page_sequence, frame_count)
    print(f"LRU: Number of page faults: {lru_faults}")

# Driver code
if __name__ == '__main__':
    simulate_page_replacement()
