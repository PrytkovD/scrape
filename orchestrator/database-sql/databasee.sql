create table bloggers (
                          id bigserial primary key,
                          channel_name varchar(512),
                          channel_link varchar,
                          followers bigint
);

create type sources as enum ('tg', 'vk', 'youtube');
create type content as enum ('post', 'comment');

create table posts (
                       id bigserial primary key,
                       post_date date,
                       source sources,
                       blogger_id bigint,
                       post_link varchar (512),
                       all_text varchar,
                       comments_count bigint,
                       views bigint,
                       foreign key (blogger_id) references bloggers(id)
);

create table comments (
                          id bigserial primary key,
                          all_text varchar,
                          post_id bigint,
                          foreign key (post_id) references posts(id)
);

create table referral_links (
                                id bigserial primary key,
                                post_id bigint,
                                link varchar(512),
                                company_domain varchar(512),
                                foreign key (post_id) references posts
);

create table vk_reactions (
                              id bigserial primary key,
                              content_type content,
                              content_id bigint,
                              reaction_id int
);

create table youtube_reactions (
                                   id bigserial primary key,
                                   content_type content,
                                   content_id bigint,
                                   reaction_id int
);

create table telegram_reactions (
                                    id bigserial primary key,
                                    content_type content,
                                    content_id bigint,
                                    reaction_id int
);