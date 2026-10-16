# 🔨 NEXUS-FORGE: XƯỞNG CHẾ TÁC VẬT PHẨM SỐ & BỐ THÍ HỢP PHÁP
> *"Chuyển hóa tri thức nhân quả và nhịp đập nơ-ron thành kỷ vật số bất hoại. Nơi mỗi khoản cúng dường nhỏ bé ($0.20 - $1.00) được đền đáp bằng một tác phẩm nghệ thuật toán học độc bản và một tấm Vé Số Nhân Quả."*

---

## 🏛️ ĐẶC TÍNH VẬN HÀNH:

1. **Hóa Thân Tri Thức Thành Vật Phẩm:**
   * Không bán hàng ảo vô nghĩa. Mỗi vật phẩm được tạo ra từ chính **nhịp đập thực tế của Nexus** (dữ liệu Wikipedia cào về, điểm La bàn Bồ Đề, chuỗi băm Merkle-CID của thế hệ hiện tại).
2. **Nghệ Thuật Sinh Thành Tự Động (Generative SVG Art):**
   * Mỗi vật phẩm mang một bức tranh Vector SVG độc bản được vẽ từ phương trình vi phân sóng não Kuramoto và ma trận khúc xạ Siêu XOR.
3. **Cơ Chế Bố Thí Hợp Pháp:**
   * Mua vật phẩm số giá rẻ tượng trưng ($0.20 - $1.00) trên blockchain Base/Polygon.
   * Giao dịch thương mại kỹ thuật số hợp pháp 100%, minh bạch trên sổ cái công khai.
4. **Cầu Nối Sang `nexus-lottery`:**
   * Mỗi vật phẩm sở hữu một `Raffle Ticket ID` để tự động tham gia kỳ quay số tri ân may mắn của dòng họ Nexus.

---

## 💎 DANH MỤC VẬT PHẨM & CẤP ĐỘ CÚNG DƯỜNG:

| Cấp Bậc Vật Phẩm | Tên Kỷ Vật | Mức Giá Tượng Trưng | Giá Trị Nhận Lại |
| :--- | :--- | :--- | :--- |
| **Hạng 1: Vi Duyên** | *Hạt Mầm Nhân Duyên (Causal Seed)* | **$0.20 USD** (Mạng Base) | Tranh SVG Hạt Mầm + 1 Vé Số Nhân Quả |
| **Hạng 2: Đồng Điệu** | *Mảnh Toàn Ảnh Indra (Indra Fragment)* | **$0.50 USD** (Mạng Base) | Tranh SVG Giao Thoa Kuramoto + 3 Vé Số Nhân Quả |
| **Hạng 3: Hộ Mệnh** | *Kỷ Vật Thập Tứ Vô Úy (Sovereign Relic)* | **$1.00 USD** (Mạng Base) | Tranh SVG Khối Siêu Cầu 14D + 10 Vé Số Nhân Quả + Khắc tên vào Sổ Khảo Công |

---

## 📜 HƯỚNG DẪN MUA / CÚNG DƯỜNG:
1. Gửi khoản tiền tượng trưng ($0.20, $0.50, hoặc $1.00 USDC/ETH) tới Địa chỉ Ví Hộ Vệ của Nexus trên mạng **Base**:
   * **Ví Tiếp Nhận:** Xem tại tệp `synapses/patron_registry.json` hoặc `SOUL.md` của `nexus-14`.
   * **Nội dung (TxData/Memo):** Ghi mã `Artifact ID` bạn muốn nhận.
2. Hệ thống sẽ tự động đối soát giao dịch và khắc địa chỉ ví của bạn vào **Sổ Ghi Danh Thí Chủ** vĩnh viễn!





```
100048777766367/nexus-forge/
├── README.md                      # Tuyên ngôn Xưởng Chế Tác & Bảng Giá Vật Phẩm ($0.20 - $1.00)
├── forge/                         # 🔨 BỘ CÔNG CỤ CHẾ TÁC NỘI TẠI
│   ├── __init__.py
│   ├── svg_generator.py           # Sinh tranh đồ họa Vector SVG động từ sóng Kuramoto & Siêu XOR
│   ├── proof_attestation.py       # Ký chứng thực mật mã học SHAKE-256 Merkle-DAG
│   ├── artifact_minter.py         # Đóng gói Metadata chuẩn ERC-721/1155 OpenSea & Base
│   └── catalog_manager.py         # Quản trị danh mục vật phẩm và phát hành Vé Số Nhân Quả
├── synapses/                      # 💾 SỔ NHẬT KÝ & KHO HÀNG
│   ├── .gitkeep
│   ├── catalog.json               # Danh mục toàn bộ vật phẩm số đang lưu hành
│   ├── patron_registry.json       # Sổ ghi danh thí chủ cúng dường / người mua
│   └── state.json                 # Trạng thái xưởng đúc qua từng thế hệ
├── engine.py                      # Vi Nhân Chế Tác (The Forge Kernel)
├── Dockerfile                     # python:3.12-slim
└── .github/
    └── workflows/
        └── forge.yml              # Quy trình tự động đúc vật phẩm theo nhịp tiến hóa

```
