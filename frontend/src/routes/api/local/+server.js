export const GET = async () => {
	const response = await fetch(`http://backend:8000/api/local`, {
		method: 'GET',
		headers: {
			accept: 'application/json'
		},
		cache: 'no-store'
	});

	return response;
};
