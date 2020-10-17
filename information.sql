-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1:3306
-- Thời gian đã tạo: Th10 17, 2020 lúc 07:53 PM
-- Phiên bản máy phục vụ: 5.7.26
-- Phiên bản PHP: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `ndkm_tktt`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `information`
--

DROP TABLE IF EXISTS `information`;
CREATE TABLE IF NOT EXISTS `information` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL,
  `date_of_birth` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `information`
--

INSERT INTO `information` (`id`, `name`, `image`, `date_of_birth`, `gender`) VALUES
(47, 'ngo thi dieu linh', 'ngo_thi_dieu_linh_2020_10_18_01_34_13.jpg', '25/12/999', 'nu'),
(48, 'vu khanh linh', 'vu_khanh_linh_2020_10_18_01_34_53.jpg', '29/12/1999', 'nu'),
(49, 'nghiem dinh nam', 'nghiem_dinh_nam_2020_10_18_01_37_29.jpg', '15/10/1999', 'nam'),
(50, 'nghiem dinh nam', 'nghiem_dinh_nam_2020_10_18_01_38_39.jpg', '15/12/1999', 'nam'),
(51, 'nghiem dinh nam', 'nghiem_dinh_nam_2020_10_18_01_39_28.jpg', '15/10/1999', 'nam'),
(52, 'nghiem dinh nam', 'nghiem_dinh_nam_2020_10_18_01_40_03.jpg', '15/10/1999', 'nam'),
(53, 'vu khanhh linh', 'vu_khanhh_linh_2020_10_18_01_47_02.jpg', '20/10/1999', 'nu'),
(54, 'vu khanhh linh', 'vu_khanhh_linh_2020_10_18_01_47_13.jpg', '20/10/1999', 'nu'),
(55, 'vu khanhh linh', 'vu_khanhh_linh_2020_10_18_01_47_48.jpg', '20/10/1999', 'nu'),
(56, 'ngo thi dieu linh', 'ngo_thi_dieu_linh_2020_10_18_01_49_50.jpg', '29/12/1999', 'nu'),
(57, 'ngo thi dieu linh', 'ngo_thi_dieu_linh_2020_10_18_01_50_00.jpg', '29/12/1999', 'nu'),
(58, 'ngo thi dieu linh', 'ngo_thi_dieu_linh_2020_10_18_01_50_13.jpg', '29/12/1999', 'nu'),
(59, 'ngo thi dieu linh', 'ngo_thi_dieu_linh_2020_10_18_01_50_22.jpg', '29/12/1999', 'nu'),
(60, 'nguyen thi anh nguyet', 'nguyen_thi_anh_nguyet_2020_10_18_01_52_34.jpg', '25/09/1999', 'nu'),
(61, 'nguyen thi anh nguyet', 'nguyen_thi_anh_nguyet_2020_10_18_01_52_45.jpg', '25/09/1999', 'nu'),
(62, 'nguyen thi anh nguyet', 'nguyen_thi_anh_nguyet_2020_10_18_01_52_57.jpg', '25/09/1999', 'nu'),
(63, 'nguyen thi anh nguyet', 'nguyen_thi_anh_nguyet_2020_10_18_01_53_06.jpg', '25/09/1999', 'nu'),
(64, 'long chu', 'long_chu_2020_10_18_01_53_56.jpg', '15/07/1999', 'nam'),
(65, 'long chu', 'long_chu_2020_10_18_01_54_04.jpg', '15/07/1999', 'nam'),
(66, 'long chu', 'long_chu_2020_10_18_01_54_13.jpg', '15/07/1999', 'nam'),
(67, 'long chu', 'long_chu_2020_10_18_01_54_21.jpg', '15/07/1999', 'nam'),
(68, 'Tran Nhu Son', 'Tran_Nhu_Son_2020_10_18_01_55_32.jpg', '28/10/1998', 'nam'),
(69, 'Tran Nhu Son', 'Tran_Nhu_Son_2020_10_18_01_55_40.jpg', '28/10/1998', 'nam'),
(70, 'Tran Nhu Son', 'Tran_Nhu_Son_2020_10_18_01_55_47.jpg', '28/10/1998', 'nam'),
(71, 'Tran Nhu Son', 'Tran_Nhu_Son_2020_10_18_01_55_55.jpg', '28/10/1998', 'nam'),
(72, 'hoang van hai', 'hoang_van_hai_2020_10_18_01_57_11.jpg', '30/08/1997', 'nam'),
(73, 'hoang van hai', 'hoang_van_hai_2020_10_18_01_57_19.jpg', '30/08/1997', 'nam'),
(74, 'hoang van hai', 'hoang_van_hai_2020_10_18_01_57_26.jpg', '30/08/1997', 'nam'),
(75, 'hoang van hai', 'hoang_van_hai_2020_10_18_01_57_34.jpg', '30/08/1997', 'nam');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
