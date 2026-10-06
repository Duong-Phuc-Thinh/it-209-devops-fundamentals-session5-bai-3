# Bài 3: Xử lý xung đột phức tạp trong quá trình Rebase

## Giới thiệu
Bài tập này hướng dẫn cách xử lý xung đột Git phức tạp khi thực hiện `git rebase` qua nhiều commit. Nhánh `feature-api` và nhánh `main` cùng chỉnh sửa tệp `config.json`, dẫn đến các xung đột ở từng chặng rebase.

## Các bước thực hiện
1. Chạy chương trình Python `main.py` để tự động thiết lập kịch bản Git, tạo các commit xung đột và hướng dẫn từng bước xử lý `git rebase`.
2. Giải quyết thủ công xung đột tại từng commit.
3. Kiểm tra kết quả bằng `git status` và `git log --graph --oneline`.

## Hướng dẫn chạy chương trình
```bash
python main.py
```