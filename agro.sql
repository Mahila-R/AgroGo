-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 02, 2019 at 06:22 AM
-- Server version: 10.1.39-MariaDB
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `agro`
--

-- --------------------------------------------------------

--
-- Table structure for table `addcrop`
--

CREATE TABLE `addcrop` (
  `id` int(4) NOT NULL,
  `farmerid` int(4) NOT NULL,
  `cropid` int(4) NOT NULL,
  `cropname` varchar(50) NOT NULL,
  `duration` varchar(50) NOT NULL,
  `soiltype` varchar(50) NOT NULL,
  `desp` varchar(100) NOT NULL,
  `image` varchar(150) NOT NULL,
  `investorname` varchar(50) NOT NULL,
  `shareamount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addcrop`
--

INSERT INTO `addcrop` (`id`, `farmerid`, `cropid`, `cropname`, `duration`, `soiltype`, `desp`, `image`, `investorname`, `shareamount`) VALUES
(1, 1, 101, 'wheat', '6 months', 'red soil', '5 kilometre', 'afa5abcd7eceac5285e9464b3360fdd0.jpg', 'guna', 50),
(2, 2, 201, 'rice', '3 month', 'black soil', '3 acker', 'landscapes-cg-digital-art-manip-ocean-tropical-space-sci-fi-planets-sky-stars-pics-166864.jpg', 'guna', 40),
(3, 1, 201, 'rice', '3 month', 'black soil', '6 acker', 'fantasy-landschaft-1463570135wBW.jpg', 'sandhiya', 40),
(4, 3, 111, 'ragi', '2 month', 'red soil', '7 acker', 'fantasy-3471234_960_720.jpg', 'sandhiya', 40),
(6, 4, 101, 'wheat', '7 months', 'black soil', '5 kilometre', 'im.jpg', 'sandhiya', 40);

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(3) NOT NULL,
  `name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(10) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `adddress` varchar(50) NOT NULL,
  `usertype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `username`, `password`, `phone`, `adddress`, `usertype`) VALUES
(1, 'sin', 'sin', '1234', '9952382360', 'ttej st.cbe', 'farmer'),
(2, 'guna', 'guna', '345', '8870546052', 'ttej st.cbe', 'investor'),
(4, 'sandhiya', 'sandy', '123', '8870546052', 'coimbatore', 'investor');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addcrop`
--
ALTER TABLE `addcrop`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addcrop`
--
ALTER TABLE `addcrop`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
