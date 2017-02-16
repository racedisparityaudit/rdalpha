class AddRacesToTaxonomy < ActiveRecord::Migration[5.0]
  def change
    add_column :taxonomy_levels, :display, :string
    add_column :taxonomy_levels, :subtitle, :string
    add_column :taxonomy_levels, :white, :string
    add_column :taxonomy_levels, :mixed, :string
    add_column :taxonomy_levels, :asian, :string
    add_column :taxonomy_levels, :black, :string
    add_column :taxonomy_levels, :chinese, :string
    add_column :taxonomy_levels, :national, :string
  end
end
