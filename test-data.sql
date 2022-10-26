-- Data prepared by Aron Gu, agu1@ualberta.ca and published on Sept 28, 2022
-- Data modified by Dan Sune, sune@ualberta.ca
-- Initial set of data was provided by Davood Rafiei, drafiei@ualberta.ca, then expanded by Aron Gu, Dan Sune

PRAGMA foreign_keys = ON;

--- Users ---
insert into users values ('u1', 'Dan', 'pw123');
insert into users values ('u2', 'Penny', 'pw234');
insert into users values ('u3', 'Yeno', 'pw345');
insert into users values ('u4', 'Digby Tierney', 'pw');
insert into users values ('u5', 'Harriet Beck', 'pw');
insert into users values ('u6', 'Aron Gu', 'pw');
insert into users values ('u7', 'Jeevan Dillard', 'pw');
insert into users values ('u8', 'Laaibah Cano', 'pw');
insert into users values ('u9', 'Ameila Pike', 'pw');
insert into users values ('u10','Davood Rafiei', 'pw');
insert into users values ('u11', 'Spencer Schimdt', 'pw');
insert into users values ('u12', 'Ryder Catonio', 'pw');
insert into users values ('u13', 'Dradelli Guy', 'pw');
insert into users values ('u14', 'Aron Gu', 'pw');
insert into users values ('u15', 'Mark Sanchez', 'pw');
insert into users values ('u16', 'Marion Trap', 'pw');
insert into users values ('u17', 'Mackenzie Parks', 'pw');
insert into users values ('u18', 'Daria Blackburn', 'pw');
insert into users values ('u19', 'Samuel Dixon', 'pw');
insert into users values ('u20','Hamed Mirzaei', 'pw');
insert into users values ('u21', 'Amelia Pike', 'pw');
insert into users values ('u22', 'Quinn Mccartney', 'pw');
insert into users values ('u23', 'Brenden Akhtar', 'pw');
insert into users values ('u24', 'Catrina Maxwell', 'pw');
insert into users values ('u25', 'Darsh Snyder', 'pw');
insert into users values ('u26', 'Pheobe Shannon', 'pw');
insert into users values ('u27', 'Judy Walsh', 'pw');
insert into users values ('u28', 'Bret Bartlett', 'pw');
insert into users values ('u29', 'Diogo Lowry', 'pw');
insert into users values ('u30', 'Rudra Duke', 'pw');
insert into users values ('u31', 'Mike Smith', 'pw');
insert into users values ('u32', 'Conner Wang', 'pw');
insert into users values ('u33', 'Saim Hays', 'pw');
insert into users values ('u34', 'Jeanne Carlson', 'pw');
insert into users values ('u35', 'John-Paul Whittaker', 'pw');
insert into users values ('u36', 'Bjorn Partridge', 'pw');
insert into users values ('u37', 'Dominic Chen', 'pw');
insert into users values ('u38', 'Aleah Mendoza', 'pw');
insert into users values ('u39', 'Kiyan Underwood', 'pw');
insert into users values ('u40', 'Wendy Fernandez', 'pw');
insert into users values ('u41', 'Shamima Gonzales', 'pw');
insert into users values ('u42', 'Mike Smith', 'pw');

--- Songs ---
insert into songs values (1, 'Waka Waka(This Time For Africa)', 202);
insert into songs values (2, 'Applause', 212);
insert into songs values (3, 'Demons', 177);
insert into songs values (4, 'Counting Stars', 259);
insert into songs values (5, 'Wavin Flag', 220);
insert into songs values (6, 'Just Give Me a Reason', 242);
insert into songs values (7, 'Stronger(What Doesn`t Kill You)', 222);
insert into songs values (8, 'We Are Young', 233);
insert into songs values (9, 'Moves Like Jagger', 201);
insert into songs values (10, 'Nice for what', 210);
insert into songs values (11, 'Hold on, we are going home', 227);
insert into songs values (12, 'DJ Got Us Fallin` in Love', 221);
insert into songs values (13, 'Wild Ones', 233);
insert into songs values (14, 'Everybody Talks', 179);
insert into songs values (15, 'Good Time', 206);
insert into songs values (16, 'Blame', 214);
insert into songs values (17, 'I Need Your Love', 234);
insert into songs values (18, 'Wake Me Up', 249);
insert into songs values (19, 'Poker Face', 238);
insert into songs values (20, 'Cheap Thrills', 224);
insert into songs values (21, 'No Lie', 221);
insert into songs values (22, 'Gentleman', 194);
insert into songs values (23, 'Titanium', 245);
insert into songs values (24, 'Cool Kids', 237);
insert into songs values (25, 'Chasing The Sun', 199);
insert into songs values (26, 'We Found Love', 215);
insert into songs values (27, 'Give Me Everything', 252);
insert into songs values (28, 'Come & Get It', 231);
insert into songs values (29, 'Me and My Broken Heart', 193);
insert into songs values (30, 'Best Day of My Life', 194);
insert into songs values (31, 'International Love', 227);
insert into songs values (32, 'You Make Me Feel...', 216);
insert into songs values (33, 'Safe and Sound', 193);
insert into songs values (34, 'Burn', 231);
insert into songs values (35, 'Shut Up and Dance', 197);
insert into songs values (36, 'Want to Want Me', 207);
insert into songs values (37, 'Dynamite', 202);
insert into songs values (38, 'Feel This Moment', 229);
insert into songs values (39, 'Hall of Fame', 202);
insert into songs values (40, 'On the Floor', 231);
insert into songs values (41, 'I Feel It Coming', 269);
insert into songs values (42, 'Blinding Lights', 201);
insert into songs values (43, 'My Heart Will Go On', 280);
insert into songs values (44, 'I`m Alive', 210);
insert into songs values (45, 'Complicated', 244);
insert into songs values (46, 'Club Can`t Handle Me', 232);
insert into songs values (47, 'Wannabe', 172);
insert into songs values (48, 'Shape of You', 233);

--- Sessions ---
insert into sessions values ('u1', 1, '2022-09-27', '2022-09-28');
insert into sessions values ('u2', 2, '2022-09-25', '2022-09-27');
insert into sessions values ('u3', 3, '2022-09-24', '2022-09-25');

--- Listen ---
insert into listen values ('u1', 1, 5, 1.2);
insert into listen values ('u2', 2, 11, 2.0);
insert into listen values ('u3', 3, 40, 33);

--- Playlists ---
insert into playlists values (1, 'Fun Songs', 'u25');
insert into playlists values (2, 'Relaxing Music', 'u40');
insert into playlists values (3, 'Relaxing Music', 'u25');
insert into playlists values (4, '2010s', 'u36');
insert into playlists values (5, 'Pop Music', 'u7');
insert into playlists values (6, 'Obscene Language', 'u11');
insert into playlists values (7, 'Yolo', 'u13');
insert into playlists values (8, 'Favorites', 'u22');
insert into playlists values (9, 'Favorites', 'u22');
insert into playlists values (10, 'Wouldn`t Play Again', 'u33');
insert into playlists values (11, 'Fun Songs', 'u9');
insert into playlists values (12, 'Love These Songs!', 'u34');
insert into playlists values (13, 'Retro Music', 'u22');
insert into playlists values (14, 'Trending Songs', 'u19');
insert into playlists values (15, 'Castle Music', 'u6');
insert into playlists values (16, 'Lady Gaga', 'u17');
insert into playlists values (17, 'Sean Paul', 'u19');
insert into playlists values (18, 'Rap', 'u38');
insert into playlists values (19, 'Pop Music', 'u31');
insert into playlists values (20, 'Let`s Get It!', 'u3');
insert into playlists values (21, 'Funny Songs', 'u27');
insert into playlists values (22, 'Great', 'u24');
insert into playlists values (23, '2013 Songs', 'u26');
insert into playlists values (24, '3 Minute Songs', 'u42');
insert into playlists values (25, '30', 'u28');
insert into playlists values (26, 'Whoa', 'u9');
insert into playlists values (27, 'Lol', 'u15');
insert into playlists values (28, 'Davood`s Favorites', 'u10');
insert into playlists values (29, 'Ryder`s Favorites', 'u12');
insert into playlists values (30, 'Songs for 291', 'u10');
insert into playlists values (31, 'Cool Playlist', 'u18');

--- PlInclude ---
-- Playlist 1
insert into plinclude values (1, 35, 1);
insert into plinclude values (1, 24, 3);
insert into plinclude values (1, 9, 2);
insert into plinclude values (1, 42, 4);
insert into plinclude values (1, 25, 5);

-- Playlist 2
insert into plinclude values (2, 8, 1);
insert into plinclude values (2, 5, 2);
insert into plinclude values (2, 15, 3);
insert into plinclude values (2, 17, 4);
insert into plinclude values (2, 19, 5);
insert into plinclude values (2, 39, 6);

-- Playlist 3
insert into plinclude values (3, 5, 1);
insert into plinclude values (3, 42, 2);
insert into plinclude values (3, 43, 3);
insert into plinclude values (3, 4, 4);
insert into plinclude values (3, 13, 5);
insert into plinclude values (3, 40, 6);

-- Playlist 4
insert into plinclude values (4, 26, 1);
insert into plinclude values (4, 19, 2);
insert into plinclude values (4, 3, 3);

-- Playlist 5
insert into plinclude values (5, 11, 1);
insert into plinclude values (5, 29, 2);
insert into plinclude values (5, 34, 3);
insert into plinclude values (5, 44, 4);

-- Playlist 6
insert into plinclude values (6, 42, 1);
insert into plinclude values (6, 23, 2);
insert into plinclude values (6, 12, 3);
insert into plinclude values (6, 2, 4);
insert into plinclude values (6, 11, 5);
insert into plinclude values (6, 35, 6);
insert into plinclude values (6, 25, 7);
insert into plinclude values (6, 6, 8);
insert into plinclude values (6, 33, 9);

-- Playlist 7
insert into plinclude values (7, 31, 1);
insert into plinclude values (7, 22, 2);
insert into plinclude values (7, 13, 3);
insert into plinclude values (7, 45, 5);
insert into plinclude values (7, 27, 4);

-- Playlist 8
insert into plinclude values (8, 25, 1);
insert into plinclude values (8, 11, 2);

-- Playlist 9
insert into plinclude values (9, 41, 1);
insert into plinclude values (9, 23, 2);
insert into plinclude values (9, 16, 3);
insert into plinclude values (9, 32, 4);
insert into plinclude values (9, 10, 5);
insert into plinclude values (9, 18, 6);
insert into plinclude values (9, 25, 7);
insert into plinclude values (9, 33, 8);
insert into plinclude values (9, 8, 9);
insert into plinclude values (9, 9, 10);

-- Playlist 10
insert into plinclude values (10, 39, 1);
insert into plinclude values (10, 40, 2);
insert into plinclude values (10, 36, 3);
insert into plinclude values (10, 26, 4);
insert into plinclude values (10, 11, 5);
insert into plinclude values (10, 42, 6);
insert into plinclude values (10, 15, 7);

-- Playlist 11
insert into plinclude values (11, 8, 1);
insert into plinclude values (11, 15, 2);
insert into plinclude values (11, 13, 3);
insert into plinclude values (11, 44, 4);
insert into plinclude values (11, 20, 5);
insert into plinclude values (11, 5, 6);
insert into plinclude values (11, 27, 7);
insert into plinclude values (11, 16, 8);
insert into plinclude values (11, 38, 9);
insert into plinclude values (11, 30, 10);
insert into plinclude values (11, 23, 11);

-- Playlist 12
insert into plinclude values (12, 28, 1);
insert into plinclude values (12, 20, 2);
insert into plinclude values (12, 43, 3);

-- Playlist 14
insert into plinclude values (14, 39, 1);
insert into plinclude values (14, 20, 2);
insert into plinclude values (14, 24, 3);
insert into plinclude values (14, 27, 4);

-- Playlist 15
insert into plinclude values (15, 10, 1);
insert into plinclude values (15, 2, 2);
insert into plinclude values (15, 35, 3);

-- Playlist 16
insert into plinclude values (16, 2, 1);
insert into plinclude values (16, 13, 2);
insert into plinclude values (16, 10, 3);
insert into plinclude values (16, 14, 4);
insert into plinclude values (16, 9, 5);
insert into plinclude values (16, 29, 6);
insert into plinclude values (16, 33, 7);
insert into plinclude values (16, 20, 8);
insert into plinclude values (16, 1, 9);
insert into plinclude values (16, 40, 10);

-- Playlist 17
insert into plinclude values (17, 45, 1);
insert into plinclude values (17, 35, 2);
insert into plinclude values (17, 17, 3);
insert into plinclude values (17, 31, 4);
insert into plinclude values (17, 29, 5);
insert into plinclude values (17, 44, 6);
insert into plinclude values (17, 34, 7);
insert into plinclude values (17, 1, 8);
insert into plinclude values (17, 26, 9);
insert into plinclude values (17, 23, 10);
insert into plinclude values (17, 8, 11);
insert into plinclude values (17, 2, 12);
insert into plinclude values (17, 43, 13);
insert into plinclude values (17, 36, 14);
insert into plinclude values (17, 37, 15);
insert into plinclude values (17, 22, 16);
insert into plinclude values (17, 7, 17);

-- Playlist 18
insert into plinclude values (18, 44, 1);
insert into plinclude values (18, 41, 2);

-- Playlist 19
insert into plinclude values (19, 40, 1);
insert into plinclude values (19, 16, 2);
insert into plinclude values (19, 18, 3);
insert into plinclude values (19, 5, 4);
insert into plinclude values (19, 9, 5);
insert into plinclude values (19, 7, 6);
insert into plinclude values (19, 20, 7);

-- Playlist 20
insert into plinclude values (20, 8, 1);
insert into plinclude values (20, 2, 2);
insert into plinclude values (20, 6, 3);

-- Playlist 21
insert into plinclude values (21, 1, 1);
insert into plinclude values (21, 2, 2);
insert into plinclude values (21, 3, 3);
insert into plinclude values (21, 4, 4);
insert into plinclude values (21, 5, 5);
insert into plinclude values (21, 6, 6);
insert into plinclude values (21, 7, 7);
insert into plinclude values (21, 8, 8);
insert into plinclude values (21, 9, 9);
insert into plinclude values (21, 10, 10);
insert into plinclude values (21, 11, 11);
insert into plinclude values (21, 12, 12);
insert into plinclude values (21, 13, 13);
insert into plinclude values (21, 14, 14);
insert into plinclude values (21, 15, 15);
insert into plinclude values (21, 16, 16);
insert into plinclude values (21, 17, 17);
insert into plinclude values (21, 18, 18);
insert into plinclude values (21, 19, 19);
insert into plinclude values (21, 20, 20);
insert into plinclude values (21, 21, 21);
insert into plinclude values (21, 22, 22);
insert into plinclude values (21, 23, 23);
insert into plinclude values (21, 24, 24);
insert into plinclude values (21, 25, 25);
insert into plinclude values (21, 26, 26);
insert into plinclude values (21, 27, 27);
insert into plinclude values (21, 28, 28);
insert into plinclude values (21, 29, 29);
insert into plinclude values (21, 30, 30);
insert into plinclude values (21, 31, 31);
insert into plinclude values (21, 32, 32);
insert into plinclude values (21, 33, 33);
insert into plinclude values (21, 34, 34);
insert into plinclude values (21, 35, 35);
insert into plinclude values (21, 36, 36);
insert into plinclude values (21, 37, 37);
insert into plinclude values (21, 38, 38);
insert into plinclude values (21, 39, 39);
insert into plinclude values (21, 40, 40);
insert into plinclude values (21, 41, 41);
insert into plinclude values (21, 42, 42);
insert into plinclude values (21, 43, 43);
insert into plinclude values (21, 44, 44);
insert into plinclude values (21, 45, 45);

-- Playlist 22
insert into plinclude values (22, 45, 1);
insert into plinclude values (22, 28, 2);

-- Playlist 23
insert into plinclude values (23, 9, 1);
insert into plinclude values (23, 18, 2);

-- Playlist 24
insert into plinclude values (24, 38, 1);

-- Playlist 25
insert into plinclude values (25, 32, 1);
insert into plinclude values (25, 22, 2);
insert into plinclude values (25, 31, 3);
insert into plinclude values (25, 43, 4);
insert into plinclude values (25, 33, 5);
insert into plinclude values (25, 25, 6);
insert into plinclude values (25, 8, 7);

-- Playlist 26
insert into plinclude values (26, 10, 1);
insert into plinclude values (26, 9, 2);
insert into plinclude values (26, 8, 3);
insert into plinclude values (26, 7, 4);

-- Playlist 27
insert into plinclude values (27, 16, 1);
insert into plinclude values (27, 5, 2);
insert into plinclude values (27, 4, 3);
insert into plinclude values (27, 41, 4);
insert into plinclude values (27, 12, 5);
insert into plinclude values (27, 23, 6);

-- Playlist 28
insert into plinclude values (28, 20, 1);
insert into plinclude values (28, 21, 2);
insert into plinclude values (28, 46, 3);

-- Playlist 29
insert into plinclude values (29, 1, 1);
insert into plinclude values (29, 8, 2);
insert into plinclude values (29, 19, 3);
insert into plinclude values (29, 15, 4);
insert into plinclude values (29, 14, 5);

-- Playlist 30
insert into plinclude values (30, 10, 1);
insert into plinclude values (30, 11, 2);
insert into plinclude values (30, 20, 3);
insert into plinclude values (30, 6, 4);
insert into plinclude values (30, 5, 5);
insert into plinclude values (30, 19, 6);
insert into plinclude values (30, 28, 7);
insert into plinclude values (30, 39, 8);
insert into plinclude values (30, 15, 9);
insert into plinclude values (30, 24, 10);
insert into plinclude values (30, 33, 11);
insert into plinclude values (30, 22, 12);
insert into plinclude values (30, 32, 13);
insert into plinclude values (30, 44, 14);
insert into plinclude values (30, 36, 15);
insert into plinclude values (30, 18, 16);
insert into plinclude values (30, 3, 17);
insert into plinclude values (30, 42, 18);
insert into plinclude values (30, 25, 19);
insert into plinclude values (30, 41, 20);
insert into plinclude values (30, 35, 21);
insert into plinclude values (30, 14, 22);
insert into plinclude values (30, 38, 23);

-- Playlist 31
insert into plinclude values (31, 5, 1);
insert into plinclude values (31, 11, 2);
insert into plinclude values (31, 42, 3);
insert into plinclude values (31, 6, 4);
insert into plinclude values (31, 43, 5);
insert into plinclude values (31, 23, 6);
insert into plinclude values (31, 12, 7);
insert into plinclude values (31, 25, 8);
insert into plinclude values (31, 16, 9);
insert into plinclude values (31, 46, 10);

--- Artists ---
insert into artists values ('a1', 'Lady Gaga', 'United States', 'pw');
insert into artists values ('a2', 'OneRepublic', 'United States', 'pw');
insert into artists values ('a3', 'Imagine Dragons', 'United States', 'pw');
insert into artists values ('a4', 'PSY', 'South Korea', 'pw');
insert into artists values ('a5', 'P!nk', 'American', 'pw');
insert into artists values ('a6', 'Nate Reuss', 'American', 'pw');
insert into artists values ('a7', 'Kelly Clarkson', 'United States', 'pw');
insert into artists values ('a8', 'Janelle Monáe', 'United States', 'pw');
insert into artists values ('a9', 'Maroon 5', 'United States', 'pw');
insert into artists values ('a10', 'Drake', 'Canada', 'pw');
insert into artists values ('a11', 'Pitbull', 'American', 'pw');
insert into artists values ('a12', 'Sia', 'Australian', 'pw');
insert into artists values ('a13', 'Neon Trees', 'American', 'pw');
insert into artists values ('a14', 'Carly Rae Jepsen', 'Canada', 'pw');
insert into artists values ('a15', 'Calvin Harris', 'Scotland', 'pw');
insert into artists values ('a16', 'Ellie Goulding', 'United Kingdom', 'pw');
insert into artists values ('a17', 'Avicii', 'Swedish', 'pw');
insert into artists values ('a18', 'Sean Paul', 'Jamaica', 'pw');
insert into artists values ('a19', 'David Guetta', 'French', 'pw');
insert into artists values ('a20', 'Bob Ezrin', 'Canadian', 'pw');
insert into artists values ('a21', 'Echosmith', 'American', 'pw');
insert into artists values ('a22', 'The Wanted', 'British', 'pw');
insert into artists values ('a23', 'Selena Gomez', 'United States', 'pw');
insert into artists values ('a24', 'Rixton', 'British', 'pw');
insert into artists values ('a25', 'American Authors', 'American', 'pw');
insert into artists values ('a26', 'Cobra Starship', 'American', 'pw');
insert into artists values ('a27', 'Captial Cities', 'American', 'pw');
insert into artists values ('a28', 'WALK THE MOON', 'United States', 'pw');
insert into artists values ('a29', 'Jason Derulo', 'American', 'pw');
insert into artists values ('a30', 'Taio Cruz', 'English', 'pw');
insert into artists values ('a31', 'The Script', 'Ireland', 'pw');
insert into artists values ('a32', 'Jennifer Lopez', 'American', 'pw');
insert into artists values ('a33', 'Shakira', 'Colombia', 'pw');
insert into artists values ('a34', 'The Weeknd', 'Canada', 'pw');
insert into artists values ('a35', 'Celine Dion', 'Canada', 'pw');
insert into artists values ('a36', 'Avril Lavigne', 'Canadian', 'pw');
insert into artists values ('a37', 'Flo Rida', 'American', 'pw');
insert into artists values ('a38', 'Spice Girls', 'British', 'pw');
insert into artists values ('a39', 'Ed Sheeran', 'England', 'pw');

--- Perform ---
insert into perform values ('a1', 2);
insert into perform values ('a1', 19);
insert into perform values ('a2', 4);
insert into perform values ('a3', 3);
insert into perform values ('a4', 22);
insert into perform values ('a5', 6);
insert into perform values ('a6', 6);
insert into perform values ('a7', 7);
insert into perform values ('a8', 8);
insert into perform values ('a9', 9);
insert into perform values ('a10', 5);
insert into perform values ('a11', 12);
insert into perform values ('a11', 27);
insert into perform values ('a11', 31);
insert into perform values ('a11', 38);
insert into perform values ('a11', 40);
insert into perform values ('a12', 13);
insert into perform values ('a12', 20);
insert into perform values ('a12', 23);
insert into perform values ('a13', 14);
insert into perform values ('a14', 15);
insert into perform values ('a15', 16);
insert into perform values ('a15', 17);
insert into perform values ('a15', 26);
insert into perform values ('a16', 17);
insert into perform values ('a16', 34);
insert into perform values ('a17', 18);
insert into perform values ('a18', 20);
insert into perform values ('a18', 21);
insert into perform values ('a19', 23);
insert into perform values ('a19', 46);
insert into perform values ('a20', 10);
insert into perform values ('a20', 11);
insert into perform values ('a21', 24);
insert into perform values ('a22', 25);
insert into perform values ('a23', 28);
insert into perform values ('a24', 29);
insert into perform values ('a25', 30);
insert into perform values ('a26', 32);
insert into perform values ('a27', 33);
insert into perform values ('a28', 35);
insert into perform values ('a29', 36);
insert into perform values ('a30', 37);
insert into perform values ('a31', 39);
insert into perform values ('a32', 40);
insert into perform values ('a33', 1);
insert into perform values ('a34', 41);
insert into perform values ('a34', 42);
insert into perform values ('a35', 43);
insert into perform values ('a35', 44);
insert into perform values ('a36', 45);
insert into perform values ('a37', 46);
insert into perform values ('a38', 47);
insert into perform values ('a39', 48);