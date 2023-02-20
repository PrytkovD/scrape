from fastapi import APIRouter
from whois21 import WHOIS

router = APIRouter()


@router.get('/')
async def whois_query_org(domain_name: str):
    query = WHOIS(domain_name)

    if not query.success:
        return {'error': query.error}

    if 'ORG' not in query.whois_data:
        return {'error': 'Unknown org'}

    return {'org': query.whois_data['ORG']}
