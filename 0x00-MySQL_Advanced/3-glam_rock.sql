-- SQL script that lists all bands with Glam rock
-- as their main style, ranked by their longevity

select band_name,
CASE
    WHEN split IS NULL then (2022 - formed)
    ELSE split - formed
END AS lifespan
FROM metal_bands
where style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
