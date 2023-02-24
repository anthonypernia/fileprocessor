drop table additional_event_data;


CREATE TABLE IF NOT EXISTS additional_event_data (
    event_id VARCHAR(255) NOT NULL PRIMARY KEY,
    device_type VARCHAR(255) NOT NULL,
    other_device_data VARCHAR(255) NOT NULL,
    dummy_data VARCHAR(255)
);


INSERT INTO additional_event_data (event_id, device_type, other_device_data ) VALUES ("123abc", "phone", "abc"), ("456def", "tablet", "def");

select * from additional_event_data

select * from final_data