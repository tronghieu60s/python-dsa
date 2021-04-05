# Array

Created: Apr 4, 2021 4:18 PM
Tags: Data Structures

**Mảng (Array)** là một trong các **cấu trúc dữ liệu** cũ và **quan trọng nhất**.

**Mảng** có thể lưu giữ một số **phần tử cố định** và các phần tử này nền có cùng kiểu. **Hầu hết** các cấu trúc dữ liệu **đều sử dụng** mảng để **triển khai giải thuật**. Dưới đây là các **khái niệm quan trọng** liên quan tới **mảng:**

- **Phần Tử**: mỗi mục được lưu giữ trong một mảng được gọi là một phần tử.
- **Chỉ Mục (Index)**: mỗi vị trí của một phần tử trong một mảng có một chỉ mục số được sử dụng để nhận diện phần tử.

![https://i.imgur.com/JqTJ3zB.png](https://i.imgur.com/JqTJ3zB.png)

![https://i.imgur.com/X6rEzH8.png](https://i.imgur.com/X6rEzH8.png)

### 1. Static Array

**Static Array** (mảng tĩnh) có **độ dài cố định**, **không thể thay đổi được** và chứa n elements.

Ví dụ về **khai báo** một Static Array trong ngôn ngữ **C**:

![https://i.imgur.com/EdPEaem.png](https://i.imgur.com/EdPEaem.png)

Kích thước của mảng tĩnh là cố định và không thể thay đổi được.

### 2. Dynamic Array

Ngược lại với Static Array, **Dynamic Array** (mảng động**)** là mảng có **kích thước thay đổi được** bằng cách cho phép thêm hoặc xóa phần tử.

Dynamic Array được **dựa trên Static Array**, bằng cách **tạo thêm một mảng mới** và **copy các phần tử từ mảng cũ** **qua** ta có thể **tăng kích thước** mảng lên.

![https://i.imgur.com/iO9QAEm.png](https://i.imgur.com/iO9QAEm.png)

 Trên đây là cách thêm phần tử mới vào dynamic array.

Tìm hiểu cách triển khai một **Dynamic Array** bằng **Static Array** bằng ngôn ngữ **Java**:

[https://youtu.be/MtSDY_kuM7o](https://youtu.be/MtSDY_kuM7o)

### 3. Jagged Arrays

Jagged Arrays (hay còn gọi là **mảng nhiều chiều** hoặc **mảng răng cưa**) giải thích đơn giản thì nó **mảng trong mảng,** dữ liệu của một mảng có thể **chứa nhiều mảng** khác nhau.

![https://i.imgur.com/bNGm6Ht.png](https://i.imgur.com/bNGm6Ht.png)

Trong mảng có 3 giá trị, và 3 giá trị này lại có những mảng giá trị khác nhau.

![https://i.imgur.com/JwpnahY.jpg](https://i.imgur.com/JwpnahY.jpg)

---

Source:

- [https://codelearn.io/learning/data-structure-and-algorithms/692192](https://codelearn.io/learning/data-structure-and-algorithms/692192)
- [https://nguyenvanhieu.vn/mang-2-chieu-trong-c/](https://nguyenvanhieu.vn/mang-2-chieu-trong-c/)