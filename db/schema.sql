create table if not exists journals (
  id uuid default gen_random_uuid() primary key,
  created_at timestamp with time zone default now(),
  content text not null,
  style text default 'buffett',
  feedback text,
  mood text,
  ticker text
);
