<script>
	import melbourne from '$lib/assets/melbourne.png';
	import sydney from '$lib/assets/sydney.png';
	import london from '$lib/assets/london.png';
	import new_york from '$lib/assets/new_york.png';
	import paris from '$lib/assets/paris.png';
	import rio from '$lib/assets/rio.png';
	import tokyo from '$lib/assets/tokyo.png';
	import beijing from '$lib/assets/beijing.png';
	const cityImages = [melbourne, sydney, london, new_york, paris, rio, tokyo, beijing];
	const imageLocationMap = {
		[melbourne]: 'Melbourne',
		[sydney]: 'Sydney',
		[london]: 'London',
		[new_york]: 'New York',
		[paris]: 'Paris',
		[rio]: 'Rio',
		[tokyo]: 'Tokyo',
		[beijing]: 'Beijing'
	};

	import logo from '$lib/assets/logo.png';

	import CurrChart from '$lib/CurrChart.svelte';
	import HistChart from '$lib/HistChart.svelte';

	let data;
	const fetchData = async (location) => {
		let lat = coordinates[location]['lat'];
		let lng = coordinates[location]['lng'];
		const res = await fetch(`http://localhost:8000/api/global?lat=${lat}&lng=${lng}`);
		data = await res.json();
		console.log(data);
		// console.log(location);
	};

	let timeOptions = ['72 Hours', '48 Hours', '24 Hours', '12 Hours'];
	let time = '72 Hours';

	let locationOptions = [
		'Melbourne',
		'Sydney',
		'London',
		'New York',
		'Paris',
		'Rio',
		'Tokyo',
		'Beijing'
	];
	let location = 'Melbourne';
	$: location, fetchData(location);
	const coordinates = {
		Melbourne: {
			lat: -37.8136,
			lng: 144.9631
		},
		Sydney: {
			lat: -33.8688,
			lng: 151.2093
		},
		London: {
			lat: 51.5074,
			lng: -0.1278
		},
		'New York': {
			lat: 40.7128,
			lng: -74.006
		},
		Paris: {
			lat: 48.8566,
			lng: 2.3522
		},
		Rio: {
			lat: -22.9068,
			lng: -43.1729
		},
		Tokyo: {
			lat: 35.6895,
			lng: 139.6917
		},
		Beijing: {
			lat: 39.9042,
			lng: 116.4074
		}
	};

	// TODO: google maps coordinates input

	// TODO: add more data
	// temperature
	// pressure
	// humidity
</script>

<div class="bg-zinc-900 h-screen">
	{#if data}
		<div class="bg-zinc-800 flex flex-row items-center justify-between p-2">
			<div class="flex flex-row items-center gap-2">
				<img src={logo} alt="map logo" class="h-16" />
				<h1 class="font-semibold text-xl text-slate-200">Enviroment Monitor Dashboard</h1>
			</div>
			<div>
				<select bind:value={location}>
					{#each locationOptions as location}
						<option value={location}>{location}</option>
					{/each}
				</select>
				<select bind:value={time}>
					{#each timeOptions as time}
						<option value={time}>{time}</option>
					{/each}
				</select>
			</div>
		</div>
		<div class="flex flex-row">
			<div class="bg-zinc-700 w-max">
				{#each cityImages as image}
					<button
						on:click={() => (location = imageLocationMap[image])}
						class={`p-2 w-max ${imageLocationMap[image] == location ? 'bg-purple-600' : ''}`}
					>
						<img src={image} alt="city" class="w-16 invert" />
					</button>
				{/each}
			</div>
			<div class="flex flex-col gap-2 p-2">
				{#key data}
					<div class="bg-zinc-800 p-4 w-max rounded-md flex flex-col gap-3">
						<h1 class="text-zinc-100">Current Data:</h1>
						<div class="flex flex-row flex-wrap gap-3 w-full">
							{#each ['reducing', 'oxidising', 'pm10', 'pm2_5'] as key}
								<div class="w-[300px] bg-zinc-700">
									<CurrChart chartData={data} dataType={key} />
								</div>
							{/each}
						</div>
					</div>
					{#key time}
						<div class="bg-zinc-800 p-4 w-max rounded-md flex flex-col gap-3">
							<h1 class="text-zinc-100">Historical Data:</h1>
							<div class="flex flex-row flex-wrap gap-3 w-full">
								{#each [['reducing', 'oxidising'], ['pm10', 'pm2_5']] as key}
									<div class="w-[480px] rounded-md p-2 bg-zinc-700">
										<HistChart chartData={data} dataTypes={key} {time} />
									</div>
								{/each}
							</div>
						</div>
					{/key}
				{/key}
			</div>
		</div>
	{:else}
		<p>data loading...</p>
	{/if}
</div>
