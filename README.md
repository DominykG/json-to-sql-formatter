# JSON to SQL formatter

## Usage
`python python .\json_to_sql.py *file_to_parse.json*`
## Example 1
Command:
`python .\json_to_sql.py .\1_article.json`

Where `.\1_article.json` contents are:
```
[
	{
		"source": "Source",
		"author": "Author",
		"title": "Title",
		"description": "Description",
		"url": "https://www.url.com/",
		"urlToImage": "https://media.urltoimage.com/image.jpg",
		"publishedAt": "2021-01-27T12:00:00Z",
		"content": "Content"
	}
]
```
The `formatted_json.sql` output file contents will look like:
```
INSERT INTO NEWS_ARTICLE (ID, SOURCE, AUTHOR, TITLE, DESCRIPTION, URL, URL_TO_IMAGE, PUBLISHED_AT, CONTENT) VALUES
(1, 'Source', 'Author', 'Title', 'Description', 'https://www.url.com/', 'https://media.urltoimage.com/image.jpg', '2021-01-27T12:00:00Z', 'Content');
```
## Example 2
Multiple JSON objects can be provided as it is shown in `2945_articles.json`.

Command:
`python .\json_to_sql.py .\2_articles.json`

The `formatted_json.sql` output file contents will look like:
```
INSERT INTO NEWS_ARTICLE (ID, SOURCE, AUTHOR, TITLE, DESCRIPTION, URL, URL_TO_IMAGE, PUBLISHED_AT, CONTENT) VALUES
(1, 'Source', 'Author', 'Title', 'Description', 'https://www.url.com/', 'https://media.urltoimage.com/image.jpg', '2021-01-27T12:00:00Z', 'Content'),
(2, 'Source2', 'Author2', 'Title2', 'Description2', 'https://www.url2.com/', 'https://media.urltoimage2.com/image.jpg', '2021-01-27T12:00:00Z', 'Content2');
```

## Configuration
The configuration file should be provided in the same directory as the `json_to_sql.py`.

In the `config.json` file has to be provided following information:
- All the illegal characters and characters they will be changed into as `"illegal_characters_to_replace"` dictionary;
- The name of the SQL table as `"table_name"` string;
- Starting index of the table as `"sql_id_start"` integer;
- All the json keys that will be parsed, if You wish to ignore some of them, illegal characters will not be removed from those keys, nor they will be inserted into .sql file. `"json_keys_to_parse"` List of String values;
- All the SQL table columns to be inserted into including primary ID as `"sql_columns"` List of String values (Note that the order in which table columns are in the `config.json` should be the same as `"json_keys_to_parse"`).
