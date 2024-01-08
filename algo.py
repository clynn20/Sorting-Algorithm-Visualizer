import pygame
from display import Display


class Algorithm(Display):
    
    def bubble_sort(self):
        n = self.barAmount
        self.sort_name = "Bubble Sort"
        self.draw_all()
        for i in range(n-1):
            for j in range(n-i-1):
                if self.barH[j] > self.barH[j+1]:
                    self.barH[j], self.barH[j+1] = self.barH[j+1], self.barH[j]
                    self.barColor[j], self.barColor[j+1] = self.barColor[j+1], self.barColor[j]
                self.draw_bars({j+1: 'green'}, True)
                self.update(100)
        self.draw_all()
        
    def selection_sort(self):
        n = self.barAmount
        self.sort_name = "Selection Sort"
        self.draw_all()
        for i in range(n):
            min_i = i
            for j in range(i+1, n):
                if self.barH[j] < self.barH[min_i]:
                    min_i = j
                self.draw_bars({min_i:'red', j:'green'},True)
                self.update(100)
            self.barH[i], self.barH[min_i] = self.barH[min_i], self.barH[i]
            self.barColor[i], self.barColor[min_i] = self.barColor[min_i], self.barColor[i]
            self.draw_bars({},True)
            self.update(100)
        self.draw_all()
    
    def insertion_sort(self):
        n = self.barAmount
        self.sort_name = "Insertion Sort"
        self.draw_all()
        for i in range (1, n):
            j = i
            #self.draw_bars({j:'green'}, True)
            #self.update(100)
            while j > 0 and self.barH[j-1] > self.barH[j]:
                self.barH[j], self.barH[j-1] = self.barH[j-1], self.barH[j]
                self.barColor[j], self.barColor[j-1] = self.barColor[j-1], self.barColor[j]
                j = j-1
                self.draw_bars({j: 'green'}, True)
                self.update(100)
        self.draw_all()
    
    def merge_sort(self, left, right):
        self.sort_name = 'Merge Sort'
        self.draw_all()
        if left < right:
            mid = left + (right - left)//2
            self.merge_sort(left, mid)
            self.merge_sort(mid+1, right)
            self.merge(left, mid, right)
        self.draw_all()
        
    def merge(self, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        L = [0]*(n1)
        R = [0]*(n2)
        LC = [0]*(n1)
        RC = [0]*(n2)
        for i in range (n1):
            L[i] = self.barH[left+i]
            LC[i] = self.barColor[left+i]
            
        for i in range (n2):
            R[i] = self.barH[mid+1+i]
            RC[i] = self.barColor[mid+1+i]
            
        i = 0
        j = 0
        k = left
        
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                self.barH[k] = L[i]
                self.barColor[k] = LC[i]
                i += 1
            else:
                self.barH[k] = R[j]
                self.barColor[k] = RC[j]
                j += 1
            k += 1
            self.draw_bars({k: 'green'}, True)
            self.update(100)
        
        while i < n1:
            self.barH[k] = L[i]
            self.barColor[k] = LC[i]
            i += 1
            k += 1
            self.draw_bars({k: 'green'}, True)
            self.update(100)
            
        while j < n2:
            self.barH[k] = R[j]
            self.barColor[k] = RC[j]
            j += 1
            k += 1
            self.draw_bars({k: 'green'}, True)
            self.update(100)
    
    def cocktail_sort(self):
        n = self.barAmount
        self.sort_name = "Cocktail Sort"
        start = 0
        end = n - 1 
        swapped = True
        self.draw_all()
        
        while swapped:
            swapped = False
            for i in range (start, end):
                if self.barH[i] > self.barH[i+1]:
                    self.barH[i], self.barH[i+1] = self.barH[i+1], self.barH[i]
                    self.barColor[i], self.barColor[i+1] = self.barColor[i+1], self.barColor[i]
                    swapped = True
                    self.draw_bars({i+1: 'green'}, True)
                    self.update(100)    
            
            if not swapped:
                break 
            
            swapped = False
            
            end -= 1
            for i in range (end-1, start-1, -1):
                if self.barH[i] > self.barH[i+1]:
                    self.barH[i], self.barH[i+1] = self.barH[i+1], self.barH[i]
                    self.barColor[i], self.barColor[i+1] = self.barColor[i+1], self.barColor[i]
                    swapped = True 
                    self.draw_bars({i: 'green'}, True)
                    self.update(100)
            start += 1
        self.draw_all()
    
    def partition(self, low, high):
        pivot = self.barH[high]
        i = low - 1
        for j in range (low, high):
            if self.barH[j] <= pivot:
                i += 1
                self.barH[i], self.barH[j] = self.barH[j], self.barH[i]
                self.barColor[i], self.barColor[j] = self.barColor[j], self.barColor[i]
                self.draw_bars({i:'green'}, True)
                self.update(100)
        self.barH[i+1], self.barH[high] = self.barH[high], self.barH[i+1]
        self.barColor[i+1], self.barColor[high] = self.barColor[high], self.barColor[i+1]
        self.draw_bars({i+1: 'green'}, True)
        self.update(100)
        return i+1
    
    def quick_sort(self, low, high):
        self.sort_name = 'Quick Sort'
        self.draw_all()
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi-1)
            self.quick_sort(pi+1, high)            
        self.draw_all()
    
    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.barH[i] < self.barH[left]:
            largest = left
        if right < n and self.barH[largest] < self.barH[right]:
            largest = right
        if largest != i:
            self.barH[i], self.barH[largest] = self.barH[largest], self.barH[i]
            self.barColor[i], self.barColor[largest] = self.barColor[i], self.barColor[largest]
            self.draw_bars({i:'green', largest:'red'}, True)
            self.update(100)
            self.heapify(n, largest)
    
    def heap_sort(self):
        n = self.barAmount
        self.sort_name = 'Heap Sort'
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        for i in range(n-1, 0, -1):
            self.barH[i], self.barH[0] = self.barH[0], self.barH[i]
            self.barColor[i], self.barColor[0] = self.barColor[0], self.barColor[i]
            self.draw_bars({i:'green'}, True)
            self.update(100)
            self.heapify(i, 0)
        self.draw_all()
        
    def countingSort(self, exp):
        n = self.barAmount
        output = [0]*(n)
        count = [0]*(10)
        
        for i in range(n):
            idx = self.barH[i] // exp
            count[idx % 10] += 1
            
        for i in range(1, 10):
            count[i] += count[i-1]
        
        i = n - 1
        while i >= 0:
             idx = self.barH[i] // exp
             output[count[idx % 10] - 1] = self.barH[i]
             count[idx % 10] -= 1
             i -= 1
        
        i = 0
        for i in range(n):
            self.barH[i] = output[i]
            self.draw_bars({i: 'green'}, True)
            self.update(100)
             
    def radix_sort(self):
        self.sort_name = 'Radix Sort'
        self.draw_all()
        max1 = max(self.barH)
        exp = 1
        while max1 // exp > 0:
            self.countingSort(exp)
            exp *= 10
        self.draw_all()