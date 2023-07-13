"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = 'playlists'

    id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True)
    name = db.Column(db.String(30),
                     nullable=False)
    description = db.Column(db.Text,
                            nullable=True)

class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = 'songs'

    id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True)
    title = db.Column(db.String(30),
                      nullable=False)
    artist = db.Column(db.String(30),
                       nullable=False)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = 'playlists_songs'

    id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.ForeignKey('playlists.id'),
                            nullable=False)
    song_id = db.Column(db.ForeignKey('songs.id'),
                        nullable=False)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
