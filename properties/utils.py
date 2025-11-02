from django_redis import get_redis_connection

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio.
    Metrics are logged (if logging is set up elsewhere).
    """
    redis_conn = get_redis_connection("default")
    info = redis_conn.info("stats")
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    hit_ratio = hits / (hits + misses)  # no 'else' clause

    print(f"Redis cache hits: {hits}, misses: {misses}, hit ratio: {hit_ratio:.2f}")
    return {
        "hits": hits,
        "misses": misses,
        "hit_ratio": hit_ratio
    }
