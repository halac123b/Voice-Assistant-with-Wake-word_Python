intent.js: Intent file đối với 1 chatbot chỉ cho nó các loại input nó có thể nhận vào và output cần trả lời tương ứng

- tag: mỗi hành động của bot đều đc phân loại cụ thể bằng 1 tag
- pattern: list các câu bot có thể xem là input đúng cho tag đó
  - Input không cần phải giống hoàn toàn, tùy vào độ thông minh của model mà bot có thể tự hiểu
  - Response: trong khi pattern có thể đc ngầm hiểu thì response từ bot sẽ là cố định và không tự phát sinh cái mới ngoài những câu trả lời ta đã quy định cho nó
