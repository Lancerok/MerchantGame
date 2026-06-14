from circular_list import CircularLinkedList

class MerchantInterface:

    def __init__(self):
        self.list_manager = CircularLinkedList()

    def _get_valid_int(self, prompt, min_val=1, max_val=None):
        while True:
            try:
                value_str = input(prompt).strip()
                
                if not value_str:
                    print("ОШИБКА | ввод не может быть пустым.")
                    continue

                value = int(value_str)

                if value < min_val:
                    print(f"ОШИБКА | значение должно быть не меньше {min_val}.")
                    continue
                
                if max_val is not None and value > max_val:
                    print(f"ОШИБКА | значение не должно превышать {max_val}.")
                    continue

                return value

            except ValueError:
                print("ОШИБКА | введите корректное целое число.")

    def run_simulation(self):
        print("\n--- Расчет расстановки груза ---")
        
        n = self._get_valid_int("Введите количество тюков у каждого купца (N): ")
        total_tubs = 2*n
        m = self._get_valid_int(
            f"Введите число месяца (M, 1-12): ", 
            min_val=1, 
            max_val=12
            
                    
        )

        k = self._get_valid_int("Введите шаг выбрасывания (K, >= 1): ")

        print(f"\nВыполняется расчет для N={n}, M={m}, K={k}...")
        
        try:
            arrangement_str = self.list_manager.create_smart_arrangement(n, m, k)
            print("\n" + "="*40)
            print("РЕЗУЛЬТАТ РАССТАНОВКИ:")
            print("="*40)
            print(arrangement_str)
            print("\nЗадача: 'Купец 1' — хитрый купец (груз останется).")
            
        except Exception as e:
            print(f"Произошла ошибка при расчете: {e}")
            
        input("\nНажмите Enter, чтобы вернуться в меню...")

    def show_menu(self):
        while True:
            print("\n" + "="*49)
            print("           ГЛАВНОЕ МЕНЮ")
            print("="*49)
            print("1. Рассчитать новую расстановку груза")
            print("2. Показать текущую структуру списка")
            print("3. Визуализировать палубу корабля (ПЛАН)")
            print("4. Показать результат шторма (ВЫБРОШЕННЫЕ)")
            print("5. ИТОГИ (СПАСЕНО/ВЫБРОШЕНО)")
            print("0. Выход из программы")
            print("-"*49)

            choice = input("Выберите действие (0-5): ").strip()

            if choice == '1':
                self.run_simulation()
            elif choice == '2':
                if self.list_manager.head:
                    self.list_manager.display()
                else:
                    print("\nСписок пуст. Сначала выполните расчет (пункт 1).")
                input("\nНажмите Enter, чтобы продолжить...")   
            
            elif choice == '3': 
                if self.list_manager.head:
                    n = self.list_manager.size // 2
                    self.list_manager.visualize_ship(n) 
                else:
                    print("\nСначала выполните расчет (пункт 1).")
                input("\nНажмите Enter, чтобы продолжить...")

            elif choice == '4':
                if self.list_manager.head and hasattr(self.list_manager, 'survivor_indices') and self.list_manager.survivor_indices:
                    self.list_manager.visualize_simulation() 
                else:
                    print("\nСначала выполните расчет (пункт 1).")
                input("\nНажмите Enter, чтобы продолжить...")

            elif choice == '5':
                if self.list_manager.head and self.list_manager.survivor_indices:
                    self.list_manager.display_simulation()
                else:
                    print("\nСначала выполните расчет (пункт 1).")
                input("\nНажмите Enter, чтобы продолжить...")

            elif choice == '0':
                print("Программа завершена. Удачи!")
                break
            else:
                print("Неверный выбор. Пожалуйста, введите 0, 1, 2, 3, 4 или 5")
