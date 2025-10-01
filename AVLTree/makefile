# Компилятор
CXX = g++

# Флаги: C++17, все предупреждения, оптимизация уровня 2
CXXFLAGS = -std=c++17 -Wall -Wextra -O2

# Имя исполняемого файла
TARGET = avl_test

# Все .cpp файлы в текущей директории
SOURCES = $(wildcard *.cpp)

# Объектные файлы
OBJECTS = $(SOURCES:.cpp=.o)

# Сборка по умолчанию
all: $(TARGET)

# Линковка
$(TARGET): $(OBJECTS)
	$(CXX) $^ -o $@

# Компиляция .cpp → .o
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Очистка
clean:
	rm -f $(OBJECTS) $(TARGET)

# Пересборка
rebuild: clean all

.PHONY: all clean rebuild
