create table bloggers (
    id bigserial primary key,
    channel_name varchar(512),
    channel_link varchar,
    followers bigint
);

create table vk_posts (
    id bigserial primary key,
    post_date date,
    blogger_id bigint,
    post_link varchar (512),
    all_text varchar,
    comments_count bigint,
    views bigint,
    foreign key (blogger_id) references bloggers(id)
);

create table youtube_posts (
    id bigserial primary key,
    post_date date,
    blogger_id bigint,
    post_link varchar (512),
    all_text varchar,
    comments_count bigint,
    views bigint,
    foreign key (blogger_id) references bloggers(id)
);

create table telegram_posts (
    id bigserial primary key,
    post_date date,
    blogger_id bigint,
    post_link varchar (512),
    all_text varchar,
    comments_count bigint,
    views bigint,
    foreign key (blogger_id) references bloggers(id)
);

create table vk_comments (
    id bigserial primary key,
    all_text varchar,
    post_id bigint,
    foreign key (post_id) references vk_posts(id)
);

create table telegram_comments (
    id bigserial primary key,
    all_text varchar,
    post_id bigint,
    foreign key (post_id) references telegram_posts(id)
);

create table youtube_comments (
    id bigserial primary key,
    all_text varchar,
    post_id bigint,
    foreign key (post_id) references youtube_posts(id)
);

create table referral_links_vk (
    id bigserial primary key,
    post_id bigint,
    link varchar(512),
    company_domain varchar(512),
    foreign key (post_id) references vk_posts
);

create table referral_links_youtube (
    id bigserial primary key,
    post_id bigint,
    link varchar(512),
    company_domain varchar(512),
    foreign key (post_id) references youtube_posts
);

create table referral_links_telegram (
    id bigserial primary key,
    post_id bigint,
    link varchar(512),
    company_domain varchar(512),
    foreign key (post_id) references telegram_posts
);

create table vk_reactions (
    id bigserial primary key,
    post_id bigint check (comment_id is null),
    comment_id bigint check (post_id is null),
    reactions_count bigint,
    _0 bigint,
    _1 bigint,
    _2 bigint,
    _3 bigint,
    _4 bigint,
    _5 bigint,
    _6 bigint,
    foreign key (post_id) references vk_posts,
    foreign key (comment_id) references vk_comments
);

create table youtube_reactions (
    id bigserial primary key,
    post_id bigint check (comment_id is null),
    comment_id bigint check (post_id is null),
    reactions_count bigint,
    likes bigint,
    dislikes bigint,
    foreign key (post_id) references youtube_posts,
    foreign key (comment_id) references youtube_comments
);

create table telegram_reactions (
    id bigserial primary key,
    post_id bigint check (comment_id is null),
    comment_id bigint check (post_id is null),
    reactions_count bigint,
    _0 bigint,
    _1 bigint,
    _2 bigint,
    _3 bigint,
    _4 bigint,
    _5 bigint,
    _6 bigint,
    _7 bigint,
    _8 bigint,
    _9 bigint,
    _10 bigint,
    _11 bigint,
    _12 bigint,
    _13 bigint,
    _14 bigint,
    _15 bigint,
    _16 bigint,
    _17 bigint,
    _18 bigint,
    _19 bigint,
    _20 bigint,
    _21 bigint,
    _22 bigint,
    _23 bigint,
    _24 bigint,
    _25 bigint,
    _26 bigint,
    _27 bigint,
    _28 bigint,
    _29 bigint,
    _30 bigint,
    _31 bigint,
    _32 bigint,
    _33 bigint,
    _34 bigint,
    _35 bigint,
    _36 bigint,
    _37 bigint,
    _38 bigint,
    _39 bigint,
    _40 bigint,
    _41 bigint,
    _42 bigint,
    _43 bigint,
    _44 bigint,
    _45 bigint,
    _46 bigint,
    _47 bigint,
    _48 bigint,
    _49 bigint,
    _50 bigint,
    _51 bigint,
    _52 bigint,
    _53 bigint,
    _54 bigint,
    _55 bigint,
    _56 bigint,
    _57 bigint,
    _58 bigint,
    _59 bigint,
    _60 bigint,
    _61 bigint,
    _62 bigint,
    _63 bigint,
    _64 bigint,
    _65 bigint,
    _66 bigint,
    foreign key (post_id) references telegram_posts,
    foreign key (comment_id) references telegram_comments
);
