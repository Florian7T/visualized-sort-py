# ALL SORTING ALGORITHMS WERE STOLEN FROM: https://stackabuse.com/sorting-algorithms-in-python/

import pygame,time,random,math
WIN_SIZE = (1920,1080)
global_size = (0,0)
PADDING = (20,20)
DELAY = 0.5 # ms

def draw():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('stop command (ALT+F4) detected. exitting now!')
            exit(0)

    screen.fill((0,0,0))
    for _ in range(num):
        if _ == ptr: pygame.draw.rect(screen,(255,0,0),pygame.Rect((_*W_AMNT+PADDING[0]+_,arr[_]*H_AMNT),(W_AMNT,WIN_SIZE[1])))
        elif _ == c_ptr: pygame.draw.rect(screen,(0,255,0),pygame.Rect((_*W_AMNT+PADDING[0]+_,arr[_]*H_AMNT),(W_AMNT,WIN_SIZE[1])))
        else: pygame.draw.rect(screen,(255,255,255),pygame.Rect((_*W_AMNT+PADDING[0]+_,arr[_]*H_AMNT),(W_AMNT,WIN_SIZE[1])))
    info_text = font.render(f"{sort_name} - {comp} comparisons, {accesed} array accesses, {DELAY}ms delay",True,(255,255,255))
    screen.blit(info_text,(WIN_SIZE[0]-info_text.get_size()[0]-50,15))
    pygame.display.flip()
    time.sleep(DELAY/1000)

def final_check(): # optional doesn't really do anything
    global ptr
    for _ in reversed(range(num)):
        ptr = _
        draw()

def insertion_sort():
    global ptr,accesed,c_ptr,comp
    for i in range (1, len (arr)):
        ptr = i
        draw()
        var = arr[i]
        j = i - 1
        accesed+=3
        comp+=2
        while j >= 0 and var < arr[j]:
            accesed+=1
            comp+=2
            arr[j + 1] = arr[j]
            ptr = j
            draw()
            j = j - 1
        c_ptr = j+1
        arr[j + 1] = var

def bubblesort():
    global ptr,accesed,c_ptr,comp
    for iter_num in range(len(arr)-1,0,-1):
        for idx in range(iter_num):
            ptr = idx
            draw()
            comp+=1
            if arr[idx]>arr[idx+1]:
                temp = arr[idx]
                arr[idx] = arr[idx+1]
                arr[idx+1] = temp
                c_ptr = idx
                accesed+=4
            accesed+=2

def selection_sort():
    global ptr,accesed,c_ptr,comp
    for i in range(len(arr)):
        l = i
        for j in range(i + 1, len(arr)):
            ptr = j
            draw()
            accesed+=2
            comp+=1
            if arr[j] < arr[l]:
                l = j
        arr[i], arr[l] = arr[l], arr[i]
        c_ptr = i
        accesed+=4

def q_partition(low, high):
    global ptr,accesed,c_ptr,comp
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        ptr = i
        draw()
        comp+=2 # 2nd loop also
        accesed+=2
        check = False
        while arr[i] < pivot:
            check = True
            comp+=1
            accesed+=1
            i += 1
        if check: # check if loop runs if so then substract the first +=
            comp-=1
            accesed-=1
        check = False
        j -= 1
        while arr[j] > pivot:
            check = True
            comp+=1
            accesed+=1
            j -= 1
        if check:
            comp-=1
            accesed-=1
        comp +=1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        c_ptr = i
        

def quick_sort():
    def _quick_sort(low, high):
        if low < high:
            split_index = q_partition(low, high)
            _quick_sort(low, split_index)
            _quick_sort(split_index + 1, high)

    _quick_sort(0, len(arr) - 1)


if __name__ == "__main__":
    arr = []
    num = input("array size ~> ")
    try: num = int(num)
    except ValueError:
        print(f"'{num}' is not a valid number")
        exit(0)
    sort = input("""Sort:
1. Selection Sort
2. Bubble Sort
3. Quick Sort
4. Insertion Sort\n~> """)
    try: sort = int(sort)
    except ValueError:
        print(f"'{sort}' is not a valid number")
        exit(0)
    W_AMNT = math.floor((WIN_SIZE[0]-PADDING[0]*2-num)/num)
    H_AMNT = math.floor((WIN_SIZE[1]-PADDING[1]*2)/num)
    if W_AMNT < 1 or H_AMNT < 1:
        print(f'an array of {num} won\'t fit on this screen')
        exit(0)
    for _ in range(1,num+1): arr.append(_)
    print(f'array: {arr}')
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE,0,32,1)
    font = pygame.font.Font(pygame.font.get_default_font(), 25)

    pygame.display.set_caption("visual sort - github.com/Florian7T")
    screen.fill((0,0,0))
    accesed = 0
    comp = 0
    ptr = -1
    c_ptr = -1
    sort_name = "Sort"
    draw()
    time.sleep(1)
    random.shuffle(arr)
    print(f'shuffled array: {arr}')
    draw()

    # where switches
    if sort == 1:
        sort_name = "Selection Sort"
        selection_sort()
    elif sort == 2:
        sort_name = "Bubble Sort"
        bubblesort()
    elif sort == 3:
        sort_name = "Quick Sort"
        quick_sort()
    elif sort == 4:
        sort_name = "Insertion Sort"
        insertion_sort()
    else:
        print(f"sort {sort} doesn't exist")
        exit(0)

    DELAY = DELAY // 2 # make unnecessary check go faster
    c_ptr = -1
    final_check()
