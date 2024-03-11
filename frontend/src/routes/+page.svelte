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
		[rio]: 'Rio de Janeiro',
		[tokyo]: 'Tokyo',
		[beijing]: 'Beijing'
	};

	import logo from '$lib/assets/logo.png';
	import info from '$lib/assets/info.png';

	import CurrChart from '$lib/CurrChart.svelte';
	import HistChart from '$lib/HistChart.svelte';

	let showInfo = false;
	let loading = true;
	let data;
	const fetchData = async (location) => {
		if (showInfo) {
			return;
		}
		let lat = coordinates[location]['lat'];
		let lng = coordinates[location]['lng'];
		const res = await fetch(`http://localhost:8000/api/global?lat=${lat}&lng=${lng}`);
		data = await res.json();
		loading = false;
		// console.log(data);
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
		'Rio de Janeiro',
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
		'Rio de Janeiro': {
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
	<div class="bg-zinc-800 flex flex-row items-center justify-between p-2">
		<div class="flex flex-row items-center gap-2">
			<img src={logo} alt="map logo" class="h-16" />
			<h1 class="font-semibold text-xl text-slate-200">Enviroment Monitor Dashboard</h1>
		</div>
		<div class="flex flex-row gap-2">
			<select
				bind:value={location}
				on:change={() => {
					loading = true;
					showInfo = false;
				}}
				class="bg-zinc-600 text-zinc-100 text-lg p-1 rounded-md"
			>
				{#each locationOptions as location}
					<option value={location}>{location}</option>
				{/each}
			</select>
			<select bind:value={time} class="bg-zinc-600 text-zinc-100 text-lg p-1 rounded-md">
				{#each timeOptions as time}
					<option value={time}>{time}</option>
				{/each}
			</select>
		</div>
	</div>
	<div class="flex flex-row">
		<div class="bg-zinc-700 w-min h-max">
			{#each cityImages as image}
				<button
					on:click={() => {
						location = imageLocationMap[image];
						loading = true;
						showInfo = false;
					}}
					class={`p-2 w-max ${imageLocationMap[image] == location ? 'bg-purple-600' : ''}`}
				>
					<img src={image} alt="city" class="w-16 invert" />
				</button>
			{/each}
			<button
				on:click={() => {
					location = '';
					showInfo = true;
				}}
				class={`flex items-center justify-center align-middle p-4 ${
					showInfo == true ? 'bg-purple-600' : ''
				}`}
			>
				<img src={info} alt="show info" class="w-14 invert" />
			</button>
		</div>
		{#if showInfo}
			<div class="flex flex-col gap-2 p-2 text-zinc-100">
				<div class="bg-zinc-800 p-4 w-[900px] rounded-md flex flex-col gap-2">
					<h1 class="text-lg font-semibold">Pollutant Types:</h1>
					<p class="text-lg">The app tracks various types of pollutants including:</p>
					<p>
						Nitrogen Dioxide (NO2): Nitrogen dioxide is a highly reactive gas formed by emissions
						from motor vehicles, industry, unflued gas-heaters and gas stove tops. High
						concentrations can be found especially near busy roads and indoors where unflued
						gas-heaters are in use. Nitrogen dioxide is a respiratory irritant and has a variety of
						adverse health effects on the respiratory system.
					</p>
					<p>
						Sulfur Dioxide (SO2): Sulphur dioxide is highly reactive gas with a pungent irritating
						smell. It is formed by fossil fuel combustion at power plants and other industrial
						facilities. Sulphur dioxide irritates the lining of the nose, throat and lungs and may
						worsen existing respiratory illness especially asthma. It has also been found to
						exacerbate cardiovascular diseases.
					</p>
					<p>
						Carbon Monoxide (CO): Carbon monoxide is a poisonous gas that you can't see, taste or
						smell. It is produced from burning fuels like gas, wood and charcoal, even if there is
						no smoke. Carbon monoxide poisoning often occurs when people use outdoor devices indoors
						or in a closed space without enough air flow.
					</p>
					<p>
						Ozone (O3): Ozone at ground level is damaging to our health. Ground level ozone is the
						main component of smog and is the product of the interaction between sunlight and
						emissions from sources such as motor vehicles and industry. Ozone can travel long
						distances and accumulate to high concentrations far away from the sources of the
						original pollutants. Ground level ozone can be harmful to our health even at low levels.
					</p>
					<p>
						Particulate Matter (PM10): With a diameter of 10 micrometers of less, these particles
						are small enough to pass through the throat and nose and enter the lungs. Once inhaled,
						these particles can affect the heart and lungs and cause serious health effects.
					</p>
					<p>
						Particulate Matter (PM2.5): With a diameter of 2.5 micrometers or less, these particles
						are so small they can get deep into the lungs and into the bloodstream. There is
						sufficient evidence that exposure to PM2.5 over long periods (years) can cause adverse
						health effects.
					</p>
				</div>
				<div class="bg-zinc-800 p-4 w-[900px] rounded-md flex flex-col gap-2">
					<h1 class="text-lg font-semibold">Data Sources:</h1>
					<p>
						The data used in this app is sourced locally in Melbourne using Enviro+. External data
						is sourced from Google Cloud's Air Quality API with a 500 x 500 meter resolution.
					</p>
				</div>
			</div>
		{:else if loading}
			<div class="p-2">
				<p class="text-slate-200 text-xl">Data Loading...</p>
			</div>
		{:else}
			<div class="flex flex-col gap-2 p-2">
				{#key data}
					<div class="bg-zinc-800 p-4 w-min rounded-md flex flex-col gap-3">
						<h1 class="text-zinc-100 text-lg">Current Data:</h1>
						<div class="flex flex-row flex-wrap gap-3 w-max">
							{#each ['no2', 'co', 'pm10', 'pm2_5'] as key}
								<div class="w-[300px] bg-zinc-700">
									<CurrChart chartData={data} dataType={key} />
								</div>
							{/each}
						</div>
					</div>
					{#key time}
						<div class="bg-zinc-800 p-4 w-max rounded-md flex flex-col gap-3">
							<h1 class="text-zinc-100 text-lg">Historical Data:</h1>
							<div class="flex flex-row flex-wrap gap-3 w-max">
								{#each [['no2', 'so2', 'co', 'o3'], ['pm10', 'pm2_5']] as key}
									<div class="w-[480px] rounded-md p-2 bg-zinc-700">
										<HistChart chartData={data} dataTypes={key} {time} />
									</div>
								{/each}
							</div>
						</div>
					{/key}
				{/key}
			</div>
		{/if}
	</div>
</div>
