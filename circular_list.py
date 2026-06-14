from node import Node

class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        self.last_n = 0
        self.last_m = 0
        self.last_k = 0
        self.survivor_indices = [] 

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.size += 1

    def get_survivor_positions(self, total_items, start_step, kill_step):
        if total_items == 0:
            return []

        indices = list(range(total_items))
        current_idx = (start_step - 1) % len(indices)
        
        while len(indices) > total_items // 2:
            indices.pop(current_idx)
            if not indices:
                break
            current_idx = (current_idx + kill_step - 1) % len(indices)
            
        return indices

    def create_smart_arrangement(self, n, m, k):
        if n <= 0:
            raise ValueError("Количество тюков (N) должно быть положительным.")
        
        total = 2 * n
        if m < 1 or m > 12:
            raise ValueError(f"Номер первого выбрасываемого (M) должен быть от 1 до 12.")

        self.last_n = n
        self.last_m = m
        self.last_k = k
        
        safe_positions = self.get_survivor_positions(total, m, k)
        self.survivor_indices = safe_positions 
        
        self.head = None
        self.size = 0
        
        arrangement = [2] * total
        for pos in safe_positions:
            arrangement[pos] = 1
            
        for owner in arrangement:
            self.append(owner)
            
        return self._format_arrangement(arrangement)

    def _format_arrangement(self, arr):
        result = []
        for i, owner in enumerate(arr):
            status = "СПАСЕН" if i in self.survivor_indices else "ВЫБРОШЕН"
            result.append(f"Тюк {i+1}: Купец {owner} ({status})")
        return "\n".join(result)

    def visualize_ship(self, n):
        if not self.head:
            print("Сначала выполните расчет!")
            return

        total = 2 * n
        
        arrangement = []
        current = self.head
        for _ in range(total):
            arrangement.append(current.data)
            current = current.next

        cell_width = 4      
        side_padding = 2    
        
        print("\n" + "=" * 60)
        print("  ВИЗУАЛИЗАЦИЯ ПАЛУБЫ КОРАБЛЯ ")
        print("=" * 60)
        
        top_border = " " * side_padding + "+" + "-" * (n * cell_width) + "+"
        print("    <--( НОС КОРАБЛЯ )")
        print(top_border)
        
        top_row_str = " " * side_padding + "|"
        for i in range(n):
            val = arrangement[i]
            cell = f" {i+1} " 
            top_row_str += cell.ljust(cell_width)
        top_row_str += "|"
        print(top_row_str)
        
        side_height = max(1, min(n // 2, 5)) 
        
        for _ in range(side_height):
            print(" " * side_padding + "|" + " " * (n * cell_width) + "|")
            
        bottom_part = list(range(n, 2*n)) 
        bottom_part.reverse() 
        
        bottom_row_str = " " * side_padding + "|"
        for val in bottom_part:
            cell = f" {val+1} "
            bottom_row_str += cell.ljust(cell_width)
        bottom_row_str += "|"
        print(bottom_row_str)
        
        print(top_border) 
        print(" " * (3*n-2) + "(   КОРМА    )-->")
        
        print(f" Параметры: N={n} (всего {total} тюков), M=мес, K=шаг")
        print("=" * 60)

    def visualize_simulation(self):
        if not self.head or not self.survivor_indices:
            print("Сначала выполните расчет (пункт 1)!")
            return

        total = self.size
        n = self.last_n if self.last_n > 0 else total // 2
        
        arrangement = []
        current = self.head
        for _ in range(total):
            arrangement.append(current.data)
            current = current.next

        print("\n" + "=" * 60)
        print("  РЕЗУЛЬТАТ ШТОРМА (ВЫБРОШЕННЫЕ ТЮКИ УДАЛЕНЫ)")
        print("=" * 60)
        
        cell_width = 4      
        side_padding = 2    
        
        top_border = " " * side_padding + "+" + "-" * (n * cell_width) + "+"
        print("    <--( НОС КОРАБЛЯ )")
        print(top_border)
        
        top_row_str = " " * side_padding + "|"
        for i in range(n):
            if i in self.survivor_indices:
                cell = f" {i+1} "
            else:
                cell = "   "
            top_row_str += cell.ljust(cell_width)
        top_row_str += "|"
        print(top_row_str)
        
        side_height = max(1, min(n // 2, 5)) 
        
        for _ in range(side_height):
            print(" " * side_padding + "|" + " " * (n * cell_width) + "|")
            
        bottom_part_indices = list(range(n, 2*n))
        bottom_part_indices.reverse()
        
        bottom_row_str = " " * side_padding + "|"
        for i in bottom_part_indices:
            if i in self.survivor_indices:
                cell = f" {i+1} "
            else:
                cell = "   "
            bottom_row_str += cell.ljust(cell_width)
        bottom_row_str += "|"
        print(bottom_row_str)
        
        print(top_border) 
        print(" " * (3*n-2) + "(   КОРМА    )-->")
        
        print(f" Параметры: N={n}, M={self.last_m}, K={self.last_k}")
        print("=" * 60)

    def display_simulation(self):
        if not self.head or not self.survivor_indices:
            print("Сначала выполните расчет (пункт 1)!")
            return

        survivors = []
        thrown = []
        
        current = self.head
        count = 0
        while True:
            if count in self.survivor_indices:
                survivors.append(f"  Тюк {count+1}: Купец {current.data} (СПАСЕН)")
            else:
                thrown.append(f"  Тюк {count+1}: Купец {current.data} (ВЫБРОШЕН)")
            
            current = current.next
            count += 1
            if current == self.head:
                break

        print("\n" + "=" * 50)
        print("        ОТЧЕТ ПО ИТОГАМ ШТОРМА")
        print("=" * 50)
        
        print("\n СПАСЕННЫЕ ТЮКИ (Остались на палубе):")
        print("-" * 50)
        if survivors:
            print("\n".join(survivors))
        else:
            print("  Нет спасенных тюков.")
            
        print(f"\n ВЫБРОШЕННЫЕ ТЮКИ (Отправлены за борт):")
        print("-" * 50)
        if thrown:
            print("\n".join(thrown))
        else:
            print("  Нет выброшенных тюков.")
            
        print("\n" + "-" * 50)
        print(f" Итого спасено: {len(survivors)} | Выброшено: {len(thrown)}")
        print("=" * 50)

    def display(self):
        if not self.head:
            print("Список пуст.")
            return
        
        current = self.head
        count = 0
        output = []
        while True:
            output.append(f"Тюк {count+1}: Купец {current.data}")
            current = current.next
            count += 1
            if current == self.head:
                break
        print("\n".join(output))
