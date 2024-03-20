export const GET = async (data) => {
	const lat = data.url.searchParams.get('lat');
	const lng = data.url.searchParams.get('lng');

	const response = await fetch(`http://backend:8000/api/global?lat=${lat}&lng=${lng}`, {
		method: 'GET',
		headers: {
			accept: 'application/json'
		},
		cache: 'no-store'
	});

	return response;
};
