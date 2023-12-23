WITH cleaned_data AS (
  -- Any necessary cleaning or transformation of raw data
  SELECT *
  FROM df_trafic1
)

SELECT *
  -- Any additional transformations or calculations you want to perform
  traveled_d / avg_speed as travel_time
FROM cleaned_data
