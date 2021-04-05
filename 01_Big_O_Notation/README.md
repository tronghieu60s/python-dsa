# Big O Notation

Created: Apr 4, 2021 4:18 PM
Tags: Data Structures

### 1. Khái niệm

Một **thuật toán** nhanh và hiệu quả **không thể đo lường qua thời gian thực**, tức là không thể đo bằng giây hoặc phút, điều này là do phần cứng máy tính. Với **cùng một chương trình**, cái của bạn có thể chạy **nhanh hoặc chậm** hơn người khác là do **phần cứng máy tính**.

![https://media.giphy.com/media/LbSdXQbS0XVVC/giphy.gif](https://media.giphy.com/media/LbSdXQbS0XVVC/giphy.gif)

Vậy, làm thế nào để **so sánh** hai thuật toán khác nhau?

Điều này có thể được đo lường qua một khái niệm gọi là **BigO Notation**.

### 2. Giải thích

Để đếm **số ký tự** trong một **chuỗi c**ách dễ nhất là **duyệt qua từng phần tử và đếm từng cái một**. Bằng cách sử dụng phương pháp này thì:

> **Thời gian cần thiết** đi qua toàn bộ chuỗi **tỷ lệ thuận** với **số lượng phần tử**.

**Đếm số ký tự** trong một chuỗi **20 ký tự** sẽ **chậm gấp 2 lần** để đếm số ký tự trong trong một chuỗi **10 ký tự**.

Thời gian chạy sẽ **tăng tuyến tính** với chiều dài đầu vào.

![https://i.imgur.com/AJ3gFcK.jpg](https://i.imgur.com/AJ3gFcK.jpg)

n là số lượng phần tử, độ phức tạp của thuật toán sẽ có giá trị là O(n).

Độ phức tạp O(n^2) **chậm hơn** đối với O(n) đó là do **số phần tử n gia tăng**, cuối cùng thì O(n^2) sẽ mất nhiều thời gian hơn.

> Nếu làm việc với một **lượng lớn dữ liệu n**, thuật toán có độ phức tạp là O(n^2) có thể làm **chậm chương trình** của bạn. Nhưng đối với **kích thước đầu vào nhỏ**, có thể bạn sẽ **không cảm thấy gì**.

![https://i.imgur.com/aW5PBel.jpg](https://i.imgur.com/aW5PBel.jpg)

### 3. Trường hợp tốt nhất và trường hợp tệ nhất

Ví dụ với thuật toán **Tìm Kiếm Tuyến Tính (Linear Search).**

Về cơ bản thuật toán này sẽ **đi qua tất cả các phần tử** trong mảng và **so sánh với giá trị cần tìm**, khi tìm thấy sẽ dừng chương trình và trả về kết quả.

![https://i.imgur.com/Ph5Ce1H.gif](https://i.imgur.com/Ph5Ce1H.gif)

Ví dụ chúng ta có mảng với các giá trị như sau: [ 1 , 2 , 3 ]

Ở **trường hợp tốt nhất** nếu phần tử cần tìm kiếm **ở đầu mảng** [ 1 , ... ], chúng ta sẽ tìm thấy nó ở bước đầu tiên, ở đây thuật toán sẽ có độ phức tạp là **O(1).**

![https://i.imgur.com/4LlHwME.jpg](https://i.imgur.com/4LlHwME.jpg)

Ngược lại, ở **trường hợp tệ nhất** phần tử cần tìm kiếm **ở cuối mảng** [ ... , 3 ], nó sẽ **duyệt qua tất cả các phần tử trong mảng** và giá trị cần tìm sẽ ở cuối cùng, độ phức tạp sẽ là **O(n).**

![https://i.imgur.com/3TLQOoI.jpg](https://i.imgur.com/3TLQOoI.jpg)

---

Source:

- [https://youtu.be/iOq5kSKqeR4](https://youtu.be/iOq5kSKqeR4)
- [https://codelearn.io/sharing/big-o-do-phuc-tap-cua-thuat-toan](https://codelearn.io/sharing/big-o-do-phuc-tap-cua-thuat-toan)
- [https://kipalog.com/posts/Bi-gau-bo-vi-khong-biet-Big-O-la-gi](https://kipalog.com/posts/Bi-gau-bo-vi-khong-biet-Big-O-la-gi)