create table review_events (
    event_id integer primary key,
    area text not null,
    status text not null,
    detail text not null
);

insert into review_events (event_id, area, status, detail) values
    (1, 'ingest', 'complete', 'source rows imported'),
    (2, 'validation', 'review', 'extraction fixture marker: shared code sample'),
    (3, 'publish', 'pending', 'snapshot waiting for approval');

select area, detail
from review_events
where status = 'review'
order by event_id;
