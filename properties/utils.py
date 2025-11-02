from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio.
    """
    redis_conn = get_redis_connection("default")  # Make sure 'default' matches your cache config
    info = redis_conn.info("stats")
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0

    logger.info(f"Redis cache hits: {hits}, misses: {misses}, hit ratio: {hit_ratio:.2f}")
    return {
        "hits": hits,
        "misses": misses,
        "hit_ratio": hit_ratio
    }

