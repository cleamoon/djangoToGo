use djangodb;

create table `tb_projects`
(
    `id` integer auto_increment comment 'project id',
    `name` varchar(50) not null comment 'project name',
    `desc` varchar(1000) not null default '' comment 'description',
    `is_good` boolean not null default 0 comment 'is it good',
    primary key (`id`)
);

create table `tb_managers`
(
    `id` integer auto_increment comment 'manager id',
    `name` varchar(20) not null comment 'manager name',
    `gender` boolean not null default 0 comment 'manager gender',
    `birthday` date not null comment 'manager birth date',
    `desc` varchar(1000) not null default '' comment 'manager description',
    `photo` varchar(255) not null default '' comment 'manager photo',
    `gcount` integer not null default 0 comment 'number of good projects',
    `bcount` integer not null default 0 comment 'number of bad projects',
    `proj_id` integer not null comment 'manager project id',
    primary key (`id`),
    foreign key (`proj_id`) references `tb_projects` (`id`)
);