const assert = require('assert');
const api = require('../api.js');
const apiKey = "ce941f39aab90056289106d7803ab71a";
var request = require('sync-request');
var keys = [
  'coord',      'weather',
  'base',       'main',
  'visibility', 'wind',
  'clouds',     'dt',
  'sys',        'timezone',
  'id',         'name',
  'cod'
]

describe('Weather API Test', () => {
	it('Server responded with a 200 using our api key.', () => {
		let apiKey = "ce941f39aab90056289106d7803ab71a";
		try{
			res1 = request('GET', "https://api.openweathermap.org/data/2.5/weather?q=San+Jose&units=imperial&appid=" + apiKey);
		}catch(e){}
		assert.strictEqual(res1.statusCode, 200, "Request returned a "+res1.statusCode+" status code.");
   	});

	it('Response contains expected json fields', () => {
                let reqData = JSON.parse(res1.getBody('utf8'));
                assert.deepEqual(Object.keys(reqData), keys);
        });
});
